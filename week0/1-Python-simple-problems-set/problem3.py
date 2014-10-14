def sum_of_divisors(n):
	sum = 0
	for x in range(1,n+1):
		if n%x==0:
			sum +=x
	return sum
def main():
	a = sum_of_divisors(7)
	print(a)
if __name__ == '__main__':
	main()