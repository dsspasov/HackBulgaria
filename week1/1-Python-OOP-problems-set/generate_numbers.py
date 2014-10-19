# generate_numbers.py
import sys
from random import randint

def generate_numbers(file_name,n):
    content= []
    for i in range(int(n)):
        content.append(str(randint(1,1000)))
    file = open(file_name,"w")
    file.write(" ".join(content))
    file.close()
def input():
    file_name = sys.argv[1]
    n = sys.argv[2]
    generate_numbers(file_name,n)
#def main():
#    input()

    #file_name = sys.argv[1]
    #n = sys.argv[2]
    #content= []
    #for i in range(int(n)):
    #    content.append(str(randint(1,1000)))
    #print(content)
    #file = open(file_name,"w")
    #file.write(" ".join(content))
    #file.close()



#if __name__ == '__main__':
#    main()