#porblem38.py
from problem4 import is_prime
def goldbach(n):
    l = []
    for i in range(1,n//2 +1):
        if is_prime(i) and is_prime(n-i):
            l.append((i,n-i))
    return l
def main():
    print( goldbach(100) )
if __name__ == '__main__':
    main()


