#problem12.py
def count_vowels(str):
	count =0
	for char in str:
		if char in "aeiouyAEIOUY":
			count = count+1
	return count
def main():
    print (count_vowels('ababab'))
if __name__ == '__main__':
    main()