import re

def repeat_substring(n,substring):
    return substring*n

def parse_marker(string):
    '''Given a string of the format '(NxN)' return a tuple of integers
    representing length of the following substring and number of times
    to repeat that substring.'''
    grammar = re.compile(r'\((\d+)x(\d+)\)')
    matches = grammar.search(string)
    return (int(matches[1]),int(matches[2]))

def part_one(string):
    total_length = 0
    stream = string[:]
    while stream:
        if not '(' in set(stream):
            total_length += len(stream)
            return total_length
        open_paren = stream.index("(")
        total_length += open_paren
        close_paren = stream.index(")")
        marker = parse_marker(stream[open_paren:close_paren+1])
        length, times = marker
        total_length += length*times
        stream = stream[close_paren+length+1:]
    return total_length

if __name__ == "__main__":
    with open("input.txt") as file:
        string = file.read()
    print(part_one(string))