from day10 import *

example_file = "test_day10input.txt"
example_list = load_file(example_file)

expected_list = [ '[({(<(())[]>[[{[]{<()<>>',
                  '[(()[<>])]({[<{<<[]>>(',
                  '{([(<{}[<>[]}>{[]{[(<()>',
                  '(((({<>}<{<{<>}{[]{[]{}',
                  '[[<[([]))<([[{}[[()]]]',
                  '[{[{({}]{}}([{[{{{}}([]',                      '{<[[]]>}<{[{[{[]{()[[[]',
                  '[<(<(<(<{}))><([]([]()',
                  '<{([([[(<>()){}]>(<<{{',
                  '<{([{{}}[<[[[<>{}]]]>[]]',
                ]

def test_file_load():
    assert example_list == expected_list

def test_check_balance():
        assert check_balance(example_list[2]) == '}'
        assert check_balance(example_list[4]) == ')'
        assert check_balance(example_list[5]) == ']'
        assert check_balance(example_list[7]) == ')'
        assert check_balance(example_list[8]) == '>'

def test_check_syntax_errors():
    assert check_syntax_errors(example_list) ==  ['}', ')', ']', ')', '>']

def test_score_errors():
    assert check_score(check_syntax_errors(example_list)) == 26397

def test_incomplete():
    assert check_balance(example_list[0]) == [']', ')', '}', ')', ']', ']', '}', '}']
    assert check_balance(example_list[1]) ==  [')', '}', ']', '>', '}', ')']
    assert check_balance(example_list[3]) == [')', ')', ')', ')', '>', '}', '>', '}', '}']

def test_check_autocomplete():
    assert check_autocomplete(example_list) == [[']', ')', '}', ')', ']', ']', '}', '}'], [')', '}', ']', '>', '}', ')'], [')', ')', ')', ')', '>', '}', '>', '}', '}'], ['>', '}', ']', '}', ']', '}', '}', ']', ']'], ['>', '}', ')', ']']]

def test_autocomplete_score():
    assert check_complete_score(check_balance(example_list[0])) == 288957
    assert check_complete_score(check_balance(example_list[1])) == 5566
    assert check_complete_score(check_balance(example_list[3])) == 1480781

def test_get_middle_score():
    assert get_middle_score(check_autocomplete(example_list)) == 288957
