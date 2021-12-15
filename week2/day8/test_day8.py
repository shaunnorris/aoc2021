from day8 import *

example_file = "test_day8input.txt"
example_list = load_file(example_file)
example_patterns = example_list[0]
example_outputs = example_list[1]
example_decoders = decode_patterns(example_patterns)

def test_loadfile():

    for output in load_file(example_file)[1]:
        assert len(output) == 4
        print(output)
    for pattern in load_file(example_file)[0]:
        assert len(pattern) == 10


def test_find_1478():
    assert find_1478(example_outputs) == 26


def test_decode_patterns():
    expected_keys = {"zero",
                      "one",
                      "two",
                      "three",
                      "four",
                      "five",
                      "six",
                      "seven",
                      "eight",
                      "nine",
                      }
    for decoder in example_decoders:
        assert set(decoder.keys()) == expected_keys
        print(decoder)

def test_find_display_numbers():
    assert find_display_numbers(example_list) == 61229

"""
def text_number_lookup():
    assert text_to_number("one") == 1
    assert text_to_number("two") == 2



"""
