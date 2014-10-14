#problem40.py
def matrix3x3(m):
    new_list=[]
    n=0
    for start in range(0,len(m),3):
        #print(start)
        #print(range(start,start+3))
        
        new_list.append([])
        new_list.append([])
        new_list.append([])
        for i in range(start,start+3):
            q=0
            #print(i)
            #012,345,678
            #end = 3
            #starte = 0
            for j in range(0,len(m),3):
                new_list[n+q]. append(m[i][j])
                new_list[n+q]. append(m[i][j+1])
                new_list[n+q]. append(m[i][j+2])
                q+=1

            #n=start
        n+=3
    return new_list
def matrix_col(m):
    new_list = [[],[],[],[],[],[],[],[],[]]
    for i in range(len(m)):
        for j in range(len(m[i])):
            new_list[j].append(m[i][j])
    return new_list
def sudoku_solved(sudoku):
    cols = matrix_col(sudoku)
    sq = matrix3x3(sudoku)
    for i in range(9):
        for each in range(1,10):
            #print(each)
            if each not in sudoku[i] or each not in cols[i] or each not in sq[i]:
                return False
    return True



def main():
    print (sudoku_solved([
        [4, 5, 2, 3, 8, 9, 7, 1, 6],
        [3, 8, 7, 4, 6, 1, 2, 9, 5],
        [6, 1, 9, 2, 5, 7, 3, 4 ,8],
        [9, 3, 5, 1, 2, 6, 8, 7, 4],
        [7, 6, 4, 9, 3, 8, 5, 2, 1],
        [1, 2, 8, 5, 7, 4, 6, 3, 9],
        [5, 7, 1, 8, 9, 2, 4, 6, 3],
        [8, 9, 6, 7, 4, 3, 1, 5 ,2],
        [2, 4, 3, 6, 1, 5, 9, 8, 7]
]))
if __name__ == '__main__':
    main()