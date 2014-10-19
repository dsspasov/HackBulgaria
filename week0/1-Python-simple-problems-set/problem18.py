#problem18.py
def is_decreasing(seq):
	for i in range(len(seq)-1):
		if seq[i]<=seq[i+1]:
			return False
	else:
		return True
def main():
	print (is_decreasing([4,3,2,1,0]))
#	a= is_decreasing([1,1,1,1,1])
#	if(a):
#		print("True")
#	else:
#		print("False")
if __name__ == '__main__':
	main()