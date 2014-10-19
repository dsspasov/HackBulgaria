#problem6.py
def sevens_in_a_row(arr,n):
	for x in range(0,len(arr)-n):
		if arr[x]==7:
			y=x
			t=n-1
			flag = True
			while flag and t!=0:
				y+=1
				if(arr[y]!=7):
					flag = False
				t-=1
			if(t==0 and flag):
				return True	
def main():
	print (sevens_in_a_row([7,2,1,6,2], 1))
#	a = sevens_in_a_row([7,2,1,6,2], 1)
#	if (a):
#		print("True")
#	else:
#		print("False")
if __name__ == '__main__':
	main()