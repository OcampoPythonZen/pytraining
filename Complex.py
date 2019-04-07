import cmath

class ComplexOp(object):

    def __init__(self,real,imaginary):
        self.real = real
        self.imaginary = imaginary

    def __repr__(self):
        return f'Número complejo:{complex(self.real,self.imaginary)}'

if __name__ == "__main__":
    obj = ComplexOp(5,3)
    print(obj)