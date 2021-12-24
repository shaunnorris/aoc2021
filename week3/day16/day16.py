#incomplete
#had to resort to reddit again after a few hours

def load_file(filename):
    with open(filename) as f:
        mylist = f.read().splitlines()
    return mylist

def decode_hex(mystring):
    keys = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
    values = ['0000',
              '0001',
              '0010',
              '0011',
              '0100',
              '0101',
              '0110',
              '0111',
              '1000',
              '1001',
              '1010',
              '1011',
              '1100',
              '1101',
              '1110',
              '1111',
              ]
    lookup = dict(zip(keys, values))
    decoded_bytes = ""
    for character in mystring:
        decoded_bytes += (lookup[character])
    return decoded_bytes

def get_packet(mybytes):
    packet = {}
    binversion = mybytes[0:3]
    packet['version'] = int(binversion, 2)
    bintype = mybytes[3:6]
    packet['type'] = int(bintype, 2)
    packetlength = 0
    if packet['type'] == 4:
        offset = 6
        morepayload = True
        binliteral = ''
        while morepayload:
            if mybytes[offset:offset+1] == '1':
                binliteral += mybytes[offset+1:offset+5]
                offset += 5
            else:
                binliteral += mybytes[offset+1:offset+5]
                morepayload = False
                binused = offset +5
        packet['payload'] = int(binliteral,2)
    else:
        packet['lengthtype'] = mybytes[6:7]
        if packet['lengthtype'] == '0':
            total_length_bits = int(mybytes[7:22],2)
            packet['total_length_bits'] = total_length_bits
            binary_payload = mybytes[22:22+total_length_bits]
            packet['subpackets'] = []
            used = 0
            payload = binary_payload
            while used < total_length_bits:
                newpacket = get_packet(payload)
                packet['subpackets'].append(newpacket)
                used += newpacket[1]
                payload = payload[used:]
            binused = 7 + total_length_bits
        elif packet['lengthtype'] == '1':
            total_subpackets = int(mybytes[7:18],2)
            packet['subpacket_count'] = total_subpackets
            packet['subpackets'] = []
            binused = offset = 18
            for x in range(total_subpackets):
                payload = mybytes[offset:]
                newpacket = get_packet(payload)
                offset += newpacket[1]
                packet['subpackets'].append(newpacket)
                binused += newpacket[1]
    print('========================')
    print(packet, binused)

    return packet, binused


def version_count(packet, count=0):
    packetbody = packet[0]
    count += int(packetbody['version'])
    if 'subpackets' in packetbody:
        for subpacket in packetbody['subpackets']:
            return version_count(subpacket, count)
    return count

puzzle_input = load_file("day16input.txt")
