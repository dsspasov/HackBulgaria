def nth_fibonacci(n):
	if n==1:
		return 1
	elif n==2:
		return 1
	else:
		return nth_fibonacci(n-1)+nth_fibonacci(n-2)
def main():
	x=nth_fibonacci(3)
	print (x)

if __name__ == '__main__':
	main()