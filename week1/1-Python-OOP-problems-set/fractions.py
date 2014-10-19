#fractions.py
class Fraction(object):
    """docstring for """
    def __init__(self, numerator,denomerator):
        self.numerator = numerator
        if(denomerator==0):
            self.denomerator = 1
        else:
            self.denomerator =denomerator
    def print(self):
        print(str(self.numerator)+'/'+str(self.denomerator))
    def __add__(self, other):
        d = self.denomerator*other.denomerator
        n = self.numerator * other.denomerator + self.denomerator*other.numerator
        return Fraction(n,d)
    def __sub__(self, other):
        d = self.denomerator*other.denomerator
        n = self.numerator * other.denomerator - self.denomerator*other.numerator
        return Fraction(n,d)

    def __mul__(self, other):
        d = self.denomerator*other.denomerator
        n = self.numerator*other.numerator
        return Fraction(n,d)

    def __eq__(self, other):
        if ((self.numerator == other.numerator) and (self.denomerator == self.denomerator)):
            return True
        else:
            return False
    def __lt__(self,other):
        f = self.numerator/self.denomerator
        s = other.numerator/other.denomerator
        if(f < s):
            return True
        else:
            return False
    def gt(self,other):
        f = self.numerator/self.denomerator
        s = other.numerator/other.denomerator
        if(f > s):
            return True
        else:
            return False
#def main():
#    a =Fraction(3,4)
#    b =Fraction(1,4)
#    x = a + b
#    y = b < a
#    print(y)
#    x.print()
#if __name__ == '__main__':
#    main()
