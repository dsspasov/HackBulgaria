#problem5.py
from problem4 import is_prime
def prime_number_of_divisors(n):
	count = 2
	for x in range(3,n):
		if(n%x==0):
			count = count +1
	if(is_prime(n)):
		return True
	else:
		return False
def main():
	print (prime_number_of_divisors(8))
#	a = prime_number_of_divisors(8)
#	if (a):
#		print("True")
#	else:
#		print("False")
if __name__ == '__main__':
	main()