def turn(starting_direction,instruction):
    '''Compute compass direction in degrees given a turn of left or right'''
    if instruction == 'L':
        return (starting_direction-90 + 360) % 360
    else:
        return (starting_direction+90 + 360) % 360 

def travel(starting_position, direction, distance):
    '''Given a starting position (distance from the origin), 
    direction and distance, compute the final destination of the 
    instruction'''
    if direction == 0:      # North
        return (starting_position[0]+distance,starting_position[1])
    if direction == 90:     # East
        return (starting_position[0],starting_position[1]+distance)
    if direction == 180:    # South
        return (starting_position[0]-distance,starting_position[1])
    if direction == 270:    # West
        return (starting_position[0],starting_position[1]-distance)


def part_one(lst):
    '''Start at the starting point and then compute the final destination
    given a series of turns and distances.  Begin facing north.
    North = 0 degrees
    East = 90 degrees
    South = 180 degrees
    West = 270 degrees'''
    position = (0,0) # rise, run
    direction = 0
    for instruction in lst:
        direction = turn(direction, instruction[0])
        distance = int(instruction[1:])
        position = travel(position, direction, distance)
    return position[0] + position[1]

def coord_range(start,stop):
    '''Return the proper range of stops given ONE AXIS depending if the 
    path goes backwards or forwards'''
    if (stop < start):
        return range(start,stop-1,-1)
    else:
        return range(start,stop+1)

def visited_blocks(start,stop):
    '''Return a set of all intersections visited when walking from one 
    block to another'''
    if start[0] == stop[0]:
        intersections = coord_range(start[1],stop[1])
        distance = abs(stop[1]-start[1])+1
        return set(zip([start[0]]*(distance),intersections))
    else:
        intersections = coord_range(start[0],stop[0])
        distance = abs(stop[0]-start[0])+1
        return set(zip(intersections,[start[1]]*(distance)))

def get_all_visited_blocks(lst):
    '''Return the first location visited twice.  Note this does not mean 
    we stopped at it necessarily, just that we walked past that block'''
    position = (0,0) # rise, run
    direction = 0
    stops = set()
    for instruction in lst:
        direction = turn(direction, instruction[0])
        distance = int(instruction[1:])
        new_position = travel(position, direction, distance)
        if new_position in stops:
            import pdb; pdb.set_trace()
            return (stops,new_position)
        else:
            stops.update(visited_blocks(position,new_position))
            position = new_position
    return (stops,position)

def part_two(lst):
    position = get_all_visited_blocks(lst)[1]
    return position[0]+position[1]

if __name__ == '__main__':
    with open('input.txt') as file:
        text = str(file.read())
        inputs = text.split(', ')
    example = ['R8', 'R4', 'R4', 'R8']
    # print(part_one(inputs))
    print(get_all_visited_blocks(example))