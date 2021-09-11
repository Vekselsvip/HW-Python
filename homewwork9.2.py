def canc(a, b, s=''):
    if s.isalpha():
        return str(a + b) + s


print(canc(10, 11, 'years'))
