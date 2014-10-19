#problem39.py
def summ(line):
    s = 0
    for i in line:
        s+=i
    return s
            
def magic_square(matrix):
    x=summ(matrix[0])

    for row in matrix:
        if x!=summ(row):
            return False
    s = 0
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            s += matrix[j][i] 
        if s!=x:
            #print(s)
            return False
        s=0
    n = len(matrix)
    s1 = 0
    for i in range(n):
        s += matrix[i][i]
        s1+= matrix[i][n-1-i]
    if s!= x or s1!=x:
        return False 
    else:
        return True
#def main():
#    print ( magic_square([[16, 23, 17], [78, 32, 21], [17, 16, 15]]) )
#if __name__ == '__main__':
#    main()
