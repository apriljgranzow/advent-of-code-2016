import solution as s

def test_top_five_letters():
    examples = {
        'aaaaa-bbb-z-y-x-' : [('a',5),('b',3),('x',1),('y',1),('z',1)],
        'a-b-c-d-e-f-g-h-' : [('a',1),('b',1),('c',1),('d',1),('e',1)],
        'not-a-real-room-' : [('o',3),('a',2),('r',2),('e',1),('l',1)]
    }
    for elem in examples:
        assert s.top_five_letters(elem) == examples[elem]

def test_frequency_string():
    examples = {
        'aaaaa-bbb-z-y-x-' : 'abxyz',
        'a-b-c-d-e-f-g-h-' : 'abcde',
        'not-a-real-room-' : 'oarel'
    }
    for elem in examples:
        assert s.frequency_string(s.top_five_letters(elem)) == examples[elem]

def test_valid_checksum():
    examples = {
        ('aaaaa-bbb-z-y-x-','abxyz') : True,
        ('a-b-c-d-e-f-g-h-','abcde') : True,
        ('not-a-real-room-','oarel') : True,
        ('totally-real-room-','decoy') : False
    }
    for elem in examples:
        assert s.valid_checksum(elem[0],elem[1]) == examples[elem]

def test_part_one():
    example =  [('aaaaa-bbb-z-y-x-',123,'abxyz'),
        ('a-b-c-d-e-f-g-h-',987,'abcde'),
        ('not-a-real-room-',404,'oarel'),
        ('totally-real-room-',200,'decoy')]
    assert s.part_one(example) == 1514
