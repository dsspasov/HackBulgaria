#concat_files.py
import sys
def get_content(file_name):
    file = open(file_name,"r")
    content = file.read()
    return content
def file_put(content):
    file_name = "MEGATRON.txt"
    file = open(file_name,"a")
    file.write(content)
    file.write('\n')
    file.close()
def main():
    files = sys.argv[1:]
    for each_file in files:
        file_put(get_content(each_file))
if __name__ == '__main__':
    main()