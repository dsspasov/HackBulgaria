#problem17.py
def is_increasing(seq):
	for i in range(len(seq)-1):
		if seq[i]>=seq[i+1]:
			return False
	else:
		return True
def main():
	print (is_increasing([5,6,-10]))
#	a= is_increasing([5,6,-10])
#	if(a):
#		print("True")
#	else:
#		print("False")
if __name__ == '__main__':
	main()