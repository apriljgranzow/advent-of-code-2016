import solution as s
from sys import maxsize

# example = 'ULL\nRRDDD\nLURDL\nUUUUD'
inputs = ['ULL','RRDDD','LURDL','UUUUD']

def test_compute_instruction():
    examples = {
        ('U',(1,1)) : (0,1),
        ('L',(0,1)) : (0,0),
        ('L',(0,0)) : (0,-1)
    }
    for elem in examples:
        assert s.compute_instruction(elem[0],elem[1]) == examples[elem]

def test_offsides():
    examples = {
       (0,0) : False,
       (0,1) : False,
       (0,2) : False,
       (1,0) : False,
       (1,1) : False,
       (1,2) : False,
       (2,0) : False,
       (2,1) : False,
       (2,2) : False,
       (-1,0) : True,
       (0,-1) : True,
       (-1,-1): True,
       (0,3) : True,
       (3,0) : True,
       (3,3) : True,
       (maxsize,0) : True,
       (maxsize*-1,0) : True,
       (0,maxsize) : True,
       (0,maxsize*-1) : True
    }
    for elem in examples:
        assert s.offsides(elem) == examples[elem]

def test_parse_instruction_line():
    examples = {
        ('ULL',(1,1)) : (0,0),
        ('RRDDD',(0,0)) : (2,2),
        ('LURDL',(2,2)) : (2,1),
        ('UUUUD',(2,1)) : (1,1)
    }
    for elem in examples:
        assert s.parse_instruction_line(elem[0],elem[1]) == examples[elem]

def test_part_one():
    assert s.part_one(inputs) == [1,9,8,5]