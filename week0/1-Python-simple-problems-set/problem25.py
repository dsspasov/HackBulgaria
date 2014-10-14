#python25.py
from math import sqrt
def prime_factorization(n):
    count= 0
    while (n%2 == 0):
        count+=1
        n = n//2

    new_list=[]
    new_list.append((2,count))

    for i in range(3,n+1,2):
        count = 0
        while (n%i == 0):
            n = n/i
            count +=1
        if(count!=0):
            new_list.append((i,count))
    if (n > 2):
        print(n)
    print(new_list)
def main():
    prime_factorization(100)
if __name__ == '__main__':
    main()