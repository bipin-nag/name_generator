
def char_range(c1, c2):
    for c in range(ord(c1), ord(c2)+1):
        yield chr(c)
    
def all():
    for c in range(ord('a'), ord('z')+1):
        yield chr(c)

def vowels():
    yield 'a'
    yield 'e'
    yield 'i'
    yield 'o'
    yield 'u'


def consonants():
    for c in range(ord('a'), ord('z')+1):
        if chr(c) not in list(vowels()):
            yield chr(c)
    

def iter_arr(s):
    arr = []
    for c in s:
        if c.lower() == "a":
            arr.append(all())
        elif c.lower() == "v":
            arr.append(vowels())
        elif c.lower() == "c":
            arr.append(consonants())
    return arr