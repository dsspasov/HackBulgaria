#problem15.py
def list_to_number(digits):
	new_list = []
	for digit in digits:
		new_list.append(str(digit))
	x = "".join(new_list)
	return int(x)
def main():
	a= list_to_number([9, 9, 9])
	print (a)
#	list_to_number(['1', '2', '3'])
if __name__ == '__main__':
	main()