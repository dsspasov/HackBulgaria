#problem11.py
#counting substrings
#ala bala ala
def counting_substrings(heystack,needle):
	count =0
	flag=True
	start=0
	if (heystack==""):
		return count
	while flag:
	    a = heystack.find(needle,start) 
	    if a==-1:      
	        flag=False
	    else:       
	        count+=1        
	        start=a+len(needle)
	if(count>0):
		return count
	else:
		return False

def main():
	print( counting_substrings("This is a test string", "is") )
#	x= counting_substrings("This is a test string", "is")
#	print(x)
if __name__ == '__main__':
	main()