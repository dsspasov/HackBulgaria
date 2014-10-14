#problem22.py
from problem11 import counting_substrings
def is_hacked(y):
	x= bin(y)
	s = str(x[2:])
	result = counting_substrings(s,"1")
	if s==s[::-1] and result%2!=0:
		return True
	else:
		return False
def is_hack(n):
	n+=1
	while(not is_hacked(n)):
		n+=1
	print (n)
	
def main():
	is_hack(10)
if __name__ == '__main__':
	main()

		