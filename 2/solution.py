# [1][2][3]     [(0,0)][(0,1)][(0,2)]
# [4][5][6]     [(1,0)][(1,1)][(1,2)]
# [7][8][9]     [(2,0)][(2,1)][(2,2)]

def convert_position_to_num(position):
    position_to_num = {
        (0,0) : 1, (0,1) : 2, (0,2) : 3,
        (1,0) : 4, (1,1) : 5, (1,2) : 6,
        (2,0) : 7, (2,1) : 8, (2,2) : 9
    }
    return position_to_num[position]

def compute_instruction(char_,start):
    '''Given a single instruction and a starting position, compute the
    position we end up on.'''
    if   char_ == 'U':
        return (start[0]-1,start[1])
    elif char_ == 'D':
        return (start[0]+1,start[1])
    elif char_ == 'L':
        return (start[0],start[1]-1)
    elif char_ == 'R':
        return (start[0],start[1]+1)

def offsides(position):
    '''Return true if the given position is off the numpad, signifying 
    an invalid move.'''
    if 0 <= position[0] <= 2 and 0 <= position[1] <= 2:
        return False
    else:
        return True

def parse_instruction_line(str_,position):
    '''Given a starting position on the keypad and a string representing
    one line of instructions, return a single digit of the password.
    If any move would cause you to move off the keypad, do not loop
    around and instead ignore those instructions.'''
    for char in str_:
        new_position = compute_instruction(char,position)
        if not offsides(new_position):
            position = new_position
    return position


def part_one(lst):
    '''Start at the 5 button and parse each line of instructions to
    return a multi-digit password'''
    position = (1,1)
    password = []
    for line in lst:
        position = parse_instruction_line(line,position)
        password.append(convert_position_to_num(position))
    return password

# Part Two: New Grid
# [.][.][1][.][.]       [  .  ][  .  ][(0,2)][  .  ][  .  ]
# [.][2][3][4][.]       [  .  ][(1,1)][(1,2)][(1,3)][  .  ]
# [5][6][7][8][9]       [(2,0)][(2,1)][(2,2)][(2,3)][(2,4)]
# [.][A][B][C][.]       [  .  ][(3,1)][(3,2)][(3,3)][  .  ]
# [.][.][D][.][.]       [  .  ][  .  ][(4,2)][  .  ][  .  ]

def offsides2(position):
    valid_positions = {(0,2),(1,1),(1,2),(1,3),(2,0),(2,1),(2,2),(2,3),
    (2,4),(3,1),(3,2),(3,3),(4,2)}
    if position not in valid_positions:
        return True
    else:
        return False

def parse_instruction_line_pt2(str_,position):
    '''Given a starting position on the keypad and a string representing
    one line of instructions, return a single digit of the password.
    If any move would cause you to move off the keypad, do not loop
    around and instead ignore those instructions.'''
    for char in str_:
        new_position = compute_instruction(char,position)
        if not offsides2(new_position):
            position = new_position
    return position

def convert_position_to_num_pt2(position):
    position_to_num = {
        (0,2):1, (1,1):2, (1,2):3, (1,3):4, (2,0):5, (2,1):6, (2,2):7,
        (2,3):8, (2,4):9, (3,1):'A', (3,2):'B', (3,3):'C', (4,2):'D'
    }
    return position_to_num[position]

def part_two(lst):
    position = (1,1)
    password = []
    for line in lst:
        position = parse_instruction_line_pt2(line,position)
        password.append(convert_position_to_num_pt2(position))
    return password

if __name__ == '__main__':
    with open('input.txt') as file:
        lines = [x.rstrip() for x in file.readlines()]
    print(part_one(lines))
    print(part_two(lines))