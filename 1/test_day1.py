import solution as s

example = ['R8', 'R4', 'R4', 'R8']

def test_travel():
    assert s.travel((0,0),90,8) == (0,8)
    assert s.travel((0,8),180,4) == (-4,8)
    assert s.travel((-4,8),270,4) == (-4,4)
    assert s.travel((-4,4),0,8) == (4,4)

def test_visited_blocks():
    assert s.visited_blocks((0,0),(0,8)) == [
            (0,0),(0,1),(0,2),(0,3),(0,4),(0,5),(0,6),(0,7),(0,8)
    ]
    assert s.visited_blocks((0,8),(-4,8)) == [(0,8),(-1,8),(-2,8),(-3,8),(-4,8)]
            

def test_get_all_visited_blocks():
    assert s.get_all_visited_blocks(example)[0] == {
        (0,0),(0,1),(0,2),(0,3),(0,4),(0,5),(0,6),(0,7),(0,8),(-1,8),
        (-2,8),(-3,8),(-4,8),(-4,7),(-4,6),(-4,5),(-4,4),(-3,4),(-2,4),
        (-1,4)
        }

def test_final_position():
    assert s.get_all_visited_blocks(example)[1] == (0,4)

def test_part_two():
    assert s.part_two(example) == 4