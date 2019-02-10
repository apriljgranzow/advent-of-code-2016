import solution as s

def test_valid_ABBA():
    examples = {
        'abba' : True,
        'bddb' : True,
        'aaaa' : False,
        'oxxo' : True,
        'mnop' : False
    }
    for elem in examples:
        assert s.valid_ABBA(elem) == examples[elem]

def test_find_ABBA():
    examples = {
        'abba' : True,
        'bddb' : True,
        'aaaa' : False,
        'oxxo' : True,
        'mnop' : False,
        'ioxxoj' : True,
        'zxcvbn' : False,
        'itgslvpxoqqokli' : True,
        'vqlnbtvojgdtchb' : False,
        'jpgwqwifygprvkyvttv' : True
    }
    for elem in examples:
        assert s.find_ABBA(elem) == examples[elem]

def test_valid_TLS():
    examples = {
        'abba[mnop]qrst' : True,
        'abcd[bddb]xyyx' : False,
        'aaaa[qwer]tyui' : False,
        'ioxxoj[asdfgh]zxcvbn' : True
    }
    for elem in examples:
        assert s.valid_TLS(elem) == examples[elem]