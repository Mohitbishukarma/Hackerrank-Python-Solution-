import math
class Complex(object):
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary
        
    def __add__(self, no):
        result = Complex((self.real+no.real),(self.imaginary+no.imaginary))
        return result
    
    def __sub__(self, no):
        result = Complex((self.real-no.real),(self.imaginary- no.imaginary))
        return result
    
    def __mul__(self, no):
        result = Complex( (self.real*no.real) - (self.imaginary*no.imaginary) , (self.real*no.imaginary) + (self.imaginary*no.real))
        return result
    
    def __truediv__(self, no):
        a = no.real
        b = no.imaginary
        c = self.real
        d = self.imaginary

        real_part = (a*c + b*d)/(a**2+b**2)
        imaginary_part = (a*d - b*c)/(a**2+b**2)
        
        result = Complex( real_part, imaginary_part)
        return result
        
    def mod(self):
        result = Complex(math.sqrt(self.real**2+self.imaginary**2),0)
        return result
    
    def __str__(self):
        if self.imaginary == 0:
            result = "%.2f+0.00i" % (self.real)
        elif self.real == 0:
            if self.imaginary >= 0:
                result = "0.00+%.2fi" % (self.imaginary)
            else:
                result = "0.00-%.2fi" % (abs(self.imaginary))
        elif self.imaginary > 0:
            result = "%.2f+%.2fi" % (self.real, self.imaginary)
        else:
            result = "%.2f-%.2fi" % (self.real, abs(self.imaginary))
        return result

if __name__ == '__main__':
    c = map(float, input().split())
    d = map(float, input().split())
    x = Complex(*c)
    y = Complex(*d)
    print(*map(str, [x+y, x-y, x*y, x/y, x.mod(), y.mod()]), sep='\n')