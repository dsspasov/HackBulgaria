def is_prime(n):
	if(n<0):
		n=-1*n
		is_prime(n)
	else:
		if n==0 or n==1:
			return False
		elif n==2:
			return True
		else:
			for x in range(2,n):
				if n%x==0:
					return False
			else:
				return True

def main():
	print(is_prime(4))
#	a = is_prime(4)
#	if (a):
#		print("True")
#	else:
#		print("False")

if __name__ == '__main__':
	main()