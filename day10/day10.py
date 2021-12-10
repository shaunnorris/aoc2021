def load_file(filename):
    with open(filename) as f:
        mylist = f.read().splitlines()
    return mylist


def check_balance(mylist):
    openers = tuple('({[<')
    closers = tuple(')}]>')
    map = dict(zip(openers, closers))
    workqueue = []

    for element in mylist:
        if element in openers:
            workqueue.append(map[element])
        elif element in closers:
            if element != workqueue.pop():
                return element
    if not workqueue:
        return True
    else:
        return workqueue


def check_syntax_errors(mylist):
    syntax_errors = []
    for line in mylist:
        result = check_balance(line)
        if not isinstance(result, list):
            syntax_errors.append(result)
    return syntax_errors

def check_autocomplete(mylist):
    completions = []
    for line in mylist:
        result = check_balance(line)
        if isinstance(result, list):
            completions.append(result)
    return completions

def check_score(error_list):
    score = 0
    chars = [')',']','}','>']
    scores = [3,57,1197,25137]
    map = dict(zip(chars, scores))
    for error in error_list:
        score = score + map[error]
    return score

def check_complete_score(complete_list):
    complete_list.reverse()
    score = 0
    chars = [')',']','}','>']
    scores = [1,2,3,4]
    map = dict(zip(chars, scores))
    for element in complete_list:
        score = score * 5 + map[element]
    return score

def get_middle_score(complete_list):
    scores = []
    for completion in complete_list:
        scores.append(check_complete_score(completion))
    scores = sorted(scores)
    middle_position = int((len(scores) -1) / 2)
    return scores[middle_position]

file = "day10input.txt"
input_list = load_file(file)
part1 = check_score(check_syntax_errors(input_list))
print(part1)
part2 = get_middle_score(check_autocomplete(input_list))
print(part2)
