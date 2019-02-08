import re
from collections import Counter

def parse_input(text):
    '''All inputs consist of lowercase letters separated by dashes,
    followed by a dash, a sector ID and a checksum in square brackets.
    This function returns a tuple of the name, ID # and checksum.'''
    grammar = re.compile(r'(.+)-(\d+)\[(.+)\]')
    return grammar.findall(text)

def top_five_letters(str_):
    letter_freqs = Counter(str_)
    del letter_freqs['-']
    return sorted(letter_freqs.most_common(), key=lambda x: (-x[1],x[0]))[:5]

def frequency_string(lst):
    return ''.join([x[0] for x in lst])

def valid_checksum(name,checksum):
    '''A room is real if the checksum is the five most common letters
    in the encrypted name, in order, with ties broken by 
    alphabetization.'''
    return frequency_string(top_five_letters(name)) == checksum

def part_one(lst):
    total = 0
    for elem in lst:
        name, number, checksum = elem
        if valid_checksum(name,checksum):
            total += int(number)
    return total

if __name__ == "__main__":
    with open("input.txt") as file:
        text = file.read()
        inputs = parse_input(text)
        print(part_one(inputs))
        