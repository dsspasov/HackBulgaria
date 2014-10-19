#problem8.py
def contains_digit(number,digit):
	while(number!=0):
		if number%10==digit:
			return True
		number = number//10
	else:
		return False
def main():
	print (contains_digit(1234,4))
#	a= contains_digit(1234,4)
#	if(a):
#		print("True")
#	else:
#		print("False")
if __name__ == '__main__':
	main()