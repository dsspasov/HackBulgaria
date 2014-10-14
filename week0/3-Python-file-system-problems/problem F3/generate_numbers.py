# generate_numbers.py
import sys
from random import randint


def main():
    file_name = sys.argv[1]
    n = sys.argv[2]
    content= []
    for i in range(int(n)):
        content.append(str(randint(1,1000)))
    #print(content)
    file = open(file_name,"w")
    file.write(" ".join(content))
    file.close()



#    print(randint(1, 1000))

if __name__ == '__main__':
    main()