import solution as s

def test_parse_marker():
    examples = {
        '(1x5)' : (1,5),
        '(3x3)' : (3,3),
        '(11x5)' : (11,5),
        '(5x11)' : (5,11),
    }
    for elem in examples:
        assert s.parse_marker(elem) == examples[elem]

def test_part_one():
    examples = {
        'ADVENT' : 6,
        'A(1x5)BC' : 7,
        '(3x3)XYZ' : 9,
        'A(2x2)BCD(2x2)EFG' : 11,
        '(6x1)(1x3)A' : 6,
        'X(8x2)(3x3)ABCY' : 18
    }
    for elem in examples:
        assert s.part_one(elem) == examples[elem]