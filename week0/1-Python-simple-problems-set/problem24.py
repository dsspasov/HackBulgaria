def iterations_of_nan_expand(expanded):
	#nStr = '000123000123'
	pattern = 'Not a'
	count =0
	flag=True
	start=0
	if (expanded==""):
		return count
	while flag:
	    a = expanded.find(pattern,start)  # find() returns -1 if the word is not found, 
	                                  #start i the starting index from the search starts(default value is 0)
	    if a==-1:          #if pattern not found set flag to False
	        flag=False
	    else:               # if word is found increase count and set starting index to a+1
	        count+=1        
	        start=a+1
	if(count>0):
		return count
	else:
		return False

def main():
	x= iterations_of_nan_expand("xasxsaxsax")
	print(x)
if __name__ == '__main__':
	main()