#python7.py
def is_int_polindrome(n):
	x= str(n);
	if(x==x[::-1]):
		return True
	else:
		return False
def main():
	a= is_int_polindrome(12)
	if(a):
		print("True")
	else:
		print("False")
if __name__ == '__main__':
	main()