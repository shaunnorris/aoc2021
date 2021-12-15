#Full Disclosure!!!
#I got stuck on this day and had to use this external help to solve
#once i had the solution worked out, i rewrote in my own style in day14.py

data = [line.strip() for line in open("day14input.txt", "r").readlines() if line.strip()]
polymer_template = data.pop(0)
insertion_rule = dict(d.split(" -> ") for d in data)

# because "AAA".count("AA") == 1 ...
def proper_substring_counter(string, substring):
    return sum(1 for i in range(len(string)) if string[i:].startswith(substring))


freqs = {pair: proper_substring_counter(polymer_template, pair) for pair in insertion_rule}
pair_sources = {pair: [] for pair in insertion_rule}
for source, insert in insertion_rule.items():
    pair_sources[source[0] + insert].append(source)
    pair_sources[insert + source[1]].append(source)


def generate_element_count(freqs, N):
    for _ in range(N):
        freqs = {p: sum(freqs[source] for source in pair_sources[p]) for p in insertion_rule}
    count = {element: 0 for pair in insertion_rule for element in pair}
    for pair, freq in freqs.items():
        count[pair[0]] += freq
        count[pair[1]] += freq

    # All elements have been counted in pairs, EXCEPT for the first and last in the template
    count[polymer_template[0]] += 1
    count[polymer_template[-1]] += 1
    return [value // 2 for value in count.values()]


print("Part 1", (lambda count: max(count) -  min(count))(generate_element_count(freqs, 10)))
print("Part 2", (lambda count: max(count) - min(count))(generate_element_count(freqs, 40)))
