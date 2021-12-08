def load_file(filename):
    patternlist = []
    displaylist = []
    with open(filename) as f:
        lines = f.readlines()
    for line in lines:
        pattern = []
        display = {}
        pattern_output = line.split('|')
        for pattern_element in pattern_output[0].split():
            pattern.append(set(pattern_element))
        for index, display_code in enumerate(pattern_output[1].split()):
            display[index] = (set(display_code))
        patternlist.append(pattern)
        displaylist.append(display)
    return patternlist, displaylist


def find_1478(output_list):
    counter = {}
    counter['i'] = 0
    counter['iv'] = 0
    counter['vii'] = 0
    counter['viii'] = 0
    for element in output_list:
        for x in range(4):
            if len(element[x]) == 2:
                counter['i'] += 1
            elif len(element[x]) == 3:
                counter['vii'] += 1
            elif len(element[x]) == 4:
                counter['iv'] += 1
            elif len(element[x]) == 7:
                counter['viii'] += 1
    return sum(counter.values())

def decode_patterns(patterns):
    decoder_list = []
    for pattern in patterns:
        decoder = {}
        for element in pattern:
            if len(element) == 2:
                decoder['one'] = element
            elif len(element) == 3:
                decoder['seven'] = element
            elif len(element) == 4:
                decoder['four'] = element
            elif len(element) == 7:
                decoder['eight'] = element
        for passtwo in pattern:
            if len(passtwo) == 5:
                seven = decoder['seven']
                if seven.issubset(passtwo):
                    decoder['three'] = passtwo
            elif len(passtwo) == 6:
                one = decoder['one']
                four = decoder['four']
                if four.issubset(passtwo):
                    decoder['nine'] = passtwo
                else:
                    if one.issubset(passtwo):
                        decoder['zero'] = passtwo
                    else:
                        decoder['six'] = passtwo
        for passthree in pattern:
            bottom_left = decoder['eight'] - decoder['nine']
            if len(passthree) == 5:
                if passthree.issubset(decoder['six']):
                    decoder['five'] = passthree
                elif bottom_left.issubset(passthree):
                    decoder['two'] = passthree
        decoder_list.append(decoder)
    return decoder_list

def find_display_numbers(data_list):
    decoders = decode_patterns(data_list[0])
    outputs = data_list[1]
    totallist = []

    for index, output in enumerate(outputs):
        #invert keys and values in decoder
        decoder = decoders[index]
        decoded = {}
        outputnum = 0
        for key,code in decoder.items():
            for position in range(4):
                if code == output[position]:
                    decoded[position] = text_to_number(key)
        outputnum += decoded[0] * 1000
        outputnum += decoded[1] * 100
        outputnum += decoded[2] * 10
        outputnum += decoded[3]

        totallist.append(outputnum)
    return sum(totallist)

def text_to_number(textnum):
    lookup = {"zero": 0,
              "one": 1,
              "two": 2,
              "three": 3,
              "four": 4,
              "five": 5,
              "six": 6,
              "seven": 7,
              "eight": 8,
              "nine": 9
              }
    return lookup[textnum]

file = "day8input.txt"
data_list = load_file(file)
patterns = data_list[0]
outputs = data_list[1]
part1 = find_1478(outputs)
print(part1)
part2 = find_display_numbers(data_list)
print(part2)
