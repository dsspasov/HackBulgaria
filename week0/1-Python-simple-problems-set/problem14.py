#problem14.py
def number_to_list(n):
	new_list = []
	while n!=0:
		new_list.append(n%10)
		n = n//10
	return new_list[::-1]
def main():
	x = number_to_list(123023)
	print (x)
if __name__ == '__main__':
	main()