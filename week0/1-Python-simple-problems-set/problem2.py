def sum_of_digits(n):
	if(n<0):
		n = n*(-1)
	sum = 0
	while(n!=0):
		sum += n%10
		n=n//10
	return sum
def main():
	x= sum_of_digits(1325132435356)
	print(x)

if __name__ == '__main__':
	main()