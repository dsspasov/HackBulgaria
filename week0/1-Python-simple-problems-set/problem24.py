def iterations_of_nan_expand(expanded):
	#nStr = '000123000123'
	pattern = 'Not a'
	count =0
	flag=True
	start=0
	if (expanded==""):
		return count
	while flag:
	    a = expanded.find(pattern,start)
	    if a==-1:          
	        flag=False
	    else:               
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