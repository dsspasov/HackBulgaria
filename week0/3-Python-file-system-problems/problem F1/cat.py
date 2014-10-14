# cat.py
import sys


def main():
    filename = sys.argv[1]
    file = open(filename, "r") # Here, "r" stands for open for reading

    # file is a file object
    # to get all the content:

    content = file.read()
    print(content)

    # when we are done, we close the file
    file.close()

if __name__ == '__main__':
    main()
