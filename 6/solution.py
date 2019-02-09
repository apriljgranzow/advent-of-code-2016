from collections import Counter

def position_counter(strings):
    '''Given n inputs of the same length k, return a list of 
    dictionaries containing character distributions keyed by index'''
    position_counts = []
    for i in range(len(strings[0])):
        position_counts.append(Counter([x[i] for x in strings]))
    return position_counts

def part_one(counter_list):
    return ''.join([str((x.most_common(1))[0][0]) for x in counter_list])



if __name__ == "__main__":
    with open("input.txt") as file:
        lines = file.read().split()
        print(part_one(position_counter(lines)))