#python21.py
from problem20 import sum_matrix
from copy import deepcopy
def make_0(l):
	for row in range(len(l)):
		for col in range(len(l[row])):
			if l[row][col]<0:
				l[row][col]=0
	return l

def matrix_bombing_plan(m):
	d = {}
	new_list = deepcopy(m)

	for i in range(len(new_list)):

		for j in range(len(new_list[i])):
			#print (new_list)
			if(i==0):
				if j==0:
					new_list[i][j+1] = new_list[i][j+1]-new_list[i][j]
					new_list[i+1][j] = new_list[i+1][j]-new_list[i][j]
					new_list[i+1][j+1] = new_list[i+1][j+1]-new_list[i][j]
				elif j== len(new_list[i])-1:
					new_list[i][j-1] = new_list[i][j-1]-new_list[i][j]
					new_list[i+1][j-1] = new_list[i+1][j-1]-new_list[i][j]
					new_list[i+1][j] = new_list[i+1][j]-new_list[i][j]
				else:
					new_list[i][j-1] = new_list[i][j-1]-new_list[i][j]
					new_list[i][j+1] = new_list[i][j+1]-new_list[i][j]

					new_list[i+1][j-1] = new_list[i+1][j-1]-new_list[i][j]
					new_list[i+1][j] = new_list[i+1][j]-new_list[i][j]
					new_list[i+1][j+1] = new_list[i+1][j+1]-new_list[i][j]
			elif i==len(new_list)-1:
				if j==0:
					new_list[i][j+1] = new_list[i][j+1]-new_list[i][j]
					new_list[i-1][j] = new_list[i-1][j]-new_list[i][j]
					new_list[i-1][j+1] = new_list[i-1][j+1]-new_list[i][j]
				elif j == len(new_list[i])-1:
					new_list[i][j-1] = new_list[i][j-1]-new_list[i][j]
					new_list[i-1][j-1] = new_list[i-1][j-1]-new_list[i][j]
					new_list[i-1][j] = new_list[i-1][j]-new_list[i][j]
				else:
					new_list[i][j-1] = new_list[i][j-1]-new_list[i][j]
					new_list[i][j+1] = new_list[i][j+1]-new_list[i][j]

					new_list[i-1][j-1] = new_list[i-1][j-1]-new_list[i][j]
					new_list[i-1][j] = new_list[i-1][j]-new_list[i][j]
					new_list[i-1][j+1] = new_list[i-1][j+1]-new_list[i][j]
			else:
				if j==0:
					new_list[i-1][j] = new_list[i-1][j]-new_list[i][j]
					new_list[i-1][j+1] = new_list[i-1][j+1]-new_list[i][j]

					new_list[i][j+1] = new_list[i][j+1]-new_list[i][j]

					new_list[i+1][j] = new_list[i+1][j]-new_list[i][j]
					new_list[i+1][j+1] = new_list[i+1][j+1]-new_list[i][j]
				elif j== len(new_list[i])-1:

					new_list[i-1][j-1] = new_list[i-1][j-1]-new_list[i][j]
					new_list[i-1][j] = new_list[i-1][j]-new_list[i][j]

					new_list[i][j-1] = new_list[i][j-1]-new_list[i][j]

					new_list[i+1][j-1] = new_list[i+1][j-1]-new_list[i][j]
					new_list[i+1][j] = new_list[i+1][j]-new_list[i][j]
				else:
					new_list[i-1][j-1] = new_list[i-1][j-1]-new_list[i][j]
					new_list[i-1][j] = new_list[i-1][j]-new_list[i][j]
					new_list[i-1][j+1] = new_list[i-1][j+1]-new_list[i][j]

					new_list[i][j-1] = new_list[i][j-1]-new_list[i][j]
			
					new_list[i][j+1] = new_list[i][j+1]-new_list[i][j]

					new_list[i+1][j-1] = new_list[i+1][j-1]-new_list[i][j]
					new_list[i+1][j] = new_list[i+1][j]-new_list[i][j]
					new_list[i+1][j+1] = new_list[i+1][j+1]-new_list[i][j]

			new_list = make_0(new_list)
			d[(i,j)] = sum_matrix(new_list)
			#print("-----------------")
			#print (new_list)
			#print("\n")
			#print(m)
			new_list = []
			new_list=deepcopy(m)
	return d


		
def  main():
		print(matrix_bombing_plan([[1,2,3],[4,5,6],[7,8,9]]))
if __name__ == '__main__':
	main()