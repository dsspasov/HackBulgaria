#sum_numbers.py
import sys
def get_content(file_name):
    file = open(file_name,"r")
    content = file.read().split(" ")
    file.close()
    return content
def sum_num(c):
    s = 0
    for each in c:
        s+=int(each)
    return s

#def main():
#    name = sys.argv[1]
#    print(sum_num(get_content(name)))

#if __name__ == '__main__':
#    main()
    