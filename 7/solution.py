import re
from collections import Counter

# separate bracketed substrings
def get_substrings(string):
    grammar = re.compile(r'(\w+|\[\w+\])')
    return grammar.findall(string)

# determine valid ABBA
def valid_ABBA(substring):
    '''An ABBA is any four-character sequence which consists of a pair 
    of two different characters followed by the reverse of that pair, 
    such as `xyyx`or `abba`.  `aaaa` is invalid; the interior characters
    must be different'''
    return (substring == substring[::-1]) and (substring[0] != substring[1])

def find_ABBA(string):
    letter_counts = Counter(string)
    chars_with_dupes = set([k for k in letter_counts if letter_counts[k] > 1])
    for i in range(0,len(string)-3):
        if string[i] in chars_with_dupes and valid_ABBA(string[i:i+4]):
            return True
    return False

# determine valid TLS
def valid_TLS(string):
    substrings = get_substrings(string)
    bracket_ABBA = False
    non_bracket_ABBA = False
    for substring in substrings:
        if substring[0] == '[' and find_ABBA(substring):
            bracket_ABBA = True
        elif find_ABBA(substring):
            non_bracket_ABBA = True
    if (non_bracket_ABBA == True) and (bracket_ABBA == False):
        return True
    else:
        return False

def part_one(strings):
    total = 0
    for string in strings:
        if valid_TLS(string):
            total += 1
    return total

if __name__ == "__main__":
    with open("input.txt") as file:
        lines = file.readlines()
    print(part_one(lines))