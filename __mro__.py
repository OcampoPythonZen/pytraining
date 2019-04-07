class A(object):
    def __init__(self):
        print('A')
        super().__init__()

class B(A):
    def __init__(self):
        print('B')
        super().__init__()

class C(A):
    def __init__(self):
        print('C')
        super().__init__()

class Z(object):
    def __init__(self):
        print('Z')
        super().__init__()

class D(C,B,Z):
    def __init__(self):
        print('D')
        super().__init__()

print('__mro__:',[x.__name__ for x in D.__mro__])
obj = D()
