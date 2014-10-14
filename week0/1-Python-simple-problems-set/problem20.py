#problem20.py
def sum_matrix(m):
	s = 0;
	for x in m:
		s +=sum(x)
	return s
def main():
	x= sum_matrix([[1,2,3]])
	print(x)
if __name__ == '__main__':
	main()