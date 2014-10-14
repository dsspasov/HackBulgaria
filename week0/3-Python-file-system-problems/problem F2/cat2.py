# cat2.py
import sys


def main():
    files = []
    files = sys.argv[1:]
    for i in files:
        file = open(i,"r")
        content = file.read()
        print(content)
        file.close()
    #print(files)
    #for i in 

if __name__ == '__main__':
    main()