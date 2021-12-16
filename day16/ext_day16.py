import sys
from dataclasses import dataclass
import binascii
import functools

@dataclass
class Packet:
    version: int
    type_id: int
    value: int

    def is_literal(self) -> bool:
        return self.type_id == 4

@dataclass
class OpPacket(Packet):
    length_type_id: int
    length_type_val: int
    sub_packets: list

def read_input() -> str:
    return sys.stdin.read().strip()

def parse_value(packet_str, i) -> int:
    value = []
    while packet_str[i] != '0':
        value.append(packet_str[i+1:i+5])
        i += 5
    value.append(packet_str[i+1:i+5])
    return i+5, int(''.join(value), 2)

def parse_type_zero(packet_str: str, index: int, length_val: int):
    packets = []
    while length_val:
        new_index, p = parse(packet_str, index)
        length_val -= new_index - index
        index = new_index
        packets.extend(p)

    return index, packets

def parse_type_one(packet_str: str, index: int, length_val: int):
    packets = []
    for _ in range(length_val):
        index, p = parse(packet_str, index)
        packets.extend(p)

    return index, packets

def parse(packet_str: str, index: int):
    packets = []

    version = int(packet_str[index:index+3], 2)
    type_id = int(packet_str[index+3:index+6], 2)

    if type_id == 4:
        index, value = parse_value(packet_str, index+6)

        packet = Packet(version=version, type_id=type_id, value=value)
        packets.append(packet)

    else:
        length_type_id = int(packet_str[index+6:index+7], 2)
        if length_type_id == 0:
            length_type_val = int(packet_str[index+7:index+22], 2)
            index, sub_packets = parse_type_zero(packet_str, index+22, length_type_val)
            packet = OpPacket(version=version,
                            type_id=type_id,
                            value=0,
                            length_type_id=length_type_id,
                            length_type_val=length_type_val,
                            sub_packets=sub_packets)
            packets.append(packet)

        else:
            length_type_val = int(packet_str[index+7:index+18], 2)
            index, sub_packets = parse_type_one(packet_str, index+18, length_type_val)
            packet = OpPacket(version=version,
                            type_id=type_id,
                            value=0,
                            length_type_id=length_type_id,
                            length_type_val=length_type_val,
                            sub_packets=sub_packets)
            packets.append(packet)

    return index, packets

def unhexify(packet_str):
    hex_to_bin = {
        '0': '0000',
        '1': '0001',
        '2': '0010',
        '3': '0011',
        '4': '0100',
        '5': '0101',
        '6': '0110',
        '7': '0111',
        '8': '1000',
        '9': '1001',
        'A': '1010',
        'B': '1011',
        'C': '1100',
        'D': '1101',
        'E': '1110',
        'F': '1111',
    }
    res = []
    for c in packet_str:
        res.append(hex_to_bin[c])
    return ''.join(res)


def sum_versions(packets):
    res = 0
    for p in packets:
        res += p.version
        if not p.is_literal():
            res += sum_versions(p.sub_packets)
    return res

def solve1():
    packet_str = unhexify(read_input())
    _, packets = parse(packet_str, 0)
    print(sum_versions(packets))

def prod(*args):
    return functools.reduce(lambda a, b : a*b, *args)

def evaluate(packet):
    if packet.is_literal():
        return packet.value

    if packet.type_id == 0:
        return sum([evaluate(sub) for sub in packet.sub_packets])
    elif packet.type_id == 1:
        return prod([evaluate(sub) for sub in packet.sub_packets])
    elif packet.type_id == 2:
        return min([evaluate(sub) for sub in packet.sub_packets])
    elif packet.type_id == 3:
        return max([evaluate(sub) for sub in packet.sub_packets])
    elif packet.type_id == 5:
        return int(evaluate(packet.sub_packets[0]) > evaluate(packet.sub_packets[1]))
    elif packet.type_id == 6:
        return int(evaluate(packet.sub_packets[0]) < evaluate(packet.sub_packets[1]))
    elif packet.type_id == 7:
        return int(evaluate(packet.sub_packets[0]) == evaluate(packet.sub_packets[1]))

def solve2():
    packet_str = unhexify(read_input())
    _, packets = parse(packet_str, 0)
    print(evaluate(packets[0]))

#solve1()

solve2()
