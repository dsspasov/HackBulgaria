#problem9.py
def mklist(n):
	a = []
	while n!=0:
		a.append(n%10)
		n = n//10
	return a[::-1]

def contains_digits(number, digits):
	a_list = []
	a_list = mklist(number)
	for x in digits:
		if x not in a_list:
			return False
	else:
		return True
def main():
	a = contains_digits(456,[])
	if(a):
		print("True")
	else:
		print("False")
if __name__ == '__main__':
	main()
