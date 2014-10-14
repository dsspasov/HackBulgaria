def remove_double_slash(path):
    while "//" in path:
        path = path.replace("//","/")
    return path

def reduce_file_path(path):
    if len(path) == 0:
        return "/"

    start = 0
    end = 0

    while "/./" in path:
        path = path.replace("/./", "/")
    i = 0
    while "/.." in path and i<=len(path)-3:
        if (path[i]+path[i+1]+path[i+2])=="/..":
            start = i
            for j in range(3, i):
                if path[j] == "/":
                    end = j
            path = path[0:end] + path[start:]
        i+=1

    if len(path)>1 and path[len(path)-1] == "/":
        path = path[:len(path)-1]
  
    path = path.replace("..", "")
    path = remove_double_slash(path)
    return path

def main():
    print(reduce_file_path(""))
    print()
    print(reduce_file_path("/hack//week0/.././week0//problem32.py/"))
    print()
    print(reduce_file_path("/srv/www/htdocs/wtf"))
    print()
    print(reduce_file_path("/srv/./././././"))
    print()
    print(reduce_file_path("/etc//wtf/"))
    print()
    print(reduce_file_path("/etc1/../etc2/../etc3/../etc4/../etc5/../etc6/../"))
    print()
    print(reduce_file_path("//////////////"))
    print()
    print(reduce_file_path("/"))
    print()
    print(reduce_file_path("/../"))

if __name__ == '__main__':
    main()
