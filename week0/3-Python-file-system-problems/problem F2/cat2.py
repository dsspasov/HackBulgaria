# cat2.py
import sys
def cat2(files):
    content = ''
    for i in files:
        file = open(i,"r")
        content += file.read()
        file.close()
    return content

#def main():
#    files = []
#    files = sys.argv[1:]
#    print(cat2(files))
    #for i in files:
    #    file = open(i,"r")
    #    content = file.read()
    #    print(content)
    #    file.close()
    #print(files)
    #for i in 

#if __name__ == '__main__':
#    main()