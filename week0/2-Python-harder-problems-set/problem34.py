#problem34.py
def nod(x,y):
    if(x==y):
        return x
    elif x>y:
        return nod(x-y,y)
    else:
        return nod(x,y-x)

def simplify_fraction(fraction):
    gcd = nod(fraction[0],fraction[1])
    simple_fraction = (fraction[0]//gcd,fraction[1]//gcd)
    return simple_fraction
def main():
    print (simplify_fraction((63,462)))
if __name__ == '__main__':
    main()