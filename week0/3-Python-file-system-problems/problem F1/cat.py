# cat.py
import sys


def cat(filename):
    file = open(filename, "r")
    content = file.read()
    file.close()
    return content

#def main():
#    filename = sys.argv[1]
#    print (cat(filename))
    #file = open(filename, "r") # Here, "r" stands for open for reading

    # file is a file object
    # to get all the content:

    #content = file.read()
    #print(content)

    # when we are done, we close the file
    #file.close()

#if __name__ == '__main__':
#    main()
