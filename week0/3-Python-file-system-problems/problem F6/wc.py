#wc.py
import sys

def chars(file_name):
    file = open(file_name , "r")
    content = file.read()
    file.close()
    return len(content)
def words(file_name):
    file = open(file_name , "r")
    contents = file.read()
    contents = contents.replace("\n\n"," ")
    content = contents.split(" ")
    file.close()
    return len(content)
def lines(file_name):
    file = open(file_name , "r")
    content = file.read().split("\n")
    file.close()    
    return len(content)

def wc_print():
    file_name = sys.argv[2]
    option = sys.argv[1]
    if option=='chars':
        print( chars(file_name) )
    elif option == 'words':
        print( words(file_name) )
    else:
        print( lines(file_name) )
#def main():
#    wc_print()
#if __name__ == '__main__':
#    main()