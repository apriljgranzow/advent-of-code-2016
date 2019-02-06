import solution as s

example = ['R8', 'R4', 'R4', 'R8']

def test_get_visited_blocks():
    assert s.get_all_visited_blocks(example)[0] == {
        (0,0),(0,1),(0,2),(0,3),(0,4),(0,5),(0,6),(0,7),(0,8),(-1,8),
        (-2,8),(-3,8),(-4,8),(-4,7),(-4,6),(-4,5),(-4,4),(-3,4),(-2,4),
        (-1,4)
        }
    