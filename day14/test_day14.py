from day14 import *

example_file = "test_day14input.txt"
example_list = load_file(example_file)

example_pairmap = example_list[0]
example_root_sequence = example_list[1]
expected_pairmap = {'CH': 'B', 'HH': 'N', 'CB': 'H', 'NH': 'C', 'HB': 'C', 'HC': 'B', 'HN': 'C', 'NN': 'C', 'BH': 'H', 'NC': 'B', 'NB': 'B', 'BN': 'B', 'BB': 'N', 'BC': 'B', 'CC': 'N', 'CN': 'C'}
expected_root_sequence = 'NNCB'

def test_file_load():
    assert example_pairmap == expected_pairmap
    assert example_root_sequence == expected_root_sequence
    assert len(example_pairmap) == 16

def test_insert_pairs():
    round1 = insert_pairs(example_pairmap, example_root_sequence)
    assert round1 == "NCNBCHB"
    round2 = insert_pairs(example_pairmap, round1)
    assert round2 == "NBCCNBBBCBHCB"
    round3 = insert_pairs(example_pairmap, round2)
    assert round3 == "NBBBCNCCNBBNBNBBCHBHHBCHB"
    round4 = insert_pairs(example_pairmap, round3)
    assert round4 == "NBBNBNBBCCNBCNCCNBBNBBNBBBNBBNBBCBHCBHHNHCBBCBHCB"

def test_map_pairs():
    assert count_elements(map1, 'N', 'B') ==  {'B': 2, 'C': 2, 'H': 1, 'N': 2}
    assert count_elements(map2, 'N', 'B') == {'B': 6, 'C': 4, 'H': 1, 'N': 2}
    #assert count_elements(example_root_map) == False

def test_multi_map():
     assert multi_map(example_pairmap, example_root_sequence, 10) ==  1588

map1 = count_pairs(example_pairmap, {'NN': 1,'NC': 1, 'CB':1})
map2 = count_pairs(example_pairmap, map1)
map3 = count_pairs(example_pairmap, map2)
