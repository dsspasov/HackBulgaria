#problem13.py
def count_consonants(str):
	count = 0
	for char in str:
		if char in "bcdfghjklmnpqrstvwxzBCDFGHJKLMNPQRSTWVXYZ":
			count = count + 1
	return count
def main():
    print (count_consonants('ababab'))
if __name__ == '__main__':
    main()