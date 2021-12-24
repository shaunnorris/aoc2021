from day16 import *

example_file = "test_day16input.txt"
example_list = load_file(example_file)


def test_simple_case():
    """
    mystring = "D2FE28"
    assert decode_hex(mystring) == '110100101111111000101000'
                    #               110100101111111000101000
def test_get_packet():
    test_bytes_a = decode_hex("D2FE28")
#    assert get_packet(test_bytes_a) == ({"version": 6,
                                      "type": 4,
                                      "payload": 2021 }, 21)
    test_bytes_b = "11010001010"
    #assert get_packet(test_bytes_b) == ({'version': 6,
                                        'type': 4,
                                        'payload': 10}, 11)
    test_bytes_c = decode_hex("38006F45291200")
    #assert get_packet(test_bytes_c) == ({'version': 1, 'type': 6,
                                        'lengthtype': '0',
                                        'total_length_bits': 27,
                                        'subpackets': [{'version': 6, 'type': 4, 'payload': 10},
                                        {'version': 2, 'type': 4, 'payload': 20}]}, 34)
    test_bytes_d = decode_hex("EE00D40C823060")
    #assert get_packet(test_bytes_d) == ({'version': 7, 'type': 3, 'lengthtype': '1', 'subpacket_count': 3, 'subpackets': [{'version': 2, 'type': 4, 'payload': 1}, {'version': 4, 'type': 4, 'payload': 2}, {'version': 1, 'type': 4, 'payload': 3}]}, 51)
    #test_bytes_e = decode_hex("8A004A801A8002F478")
    #assert get_packet(test_bytes_e) == False
    """

def test_version_count():
    test_bytes_e = decode_hex("620080001611562C8802118E34")
    packets = get_packet(test_bytes_e)
    assert version_count(packets) == 16
    
