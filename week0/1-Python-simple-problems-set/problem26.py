#python26.py
def calculate_coins(n):
	count100=0
	count50 =0
	count20 =0
	count10 =0
	count5 = 0
	count2 = 0
	count1 = 0
	d={}
	while(n>=1.0):
		count100 +=1
		n=n-1.0
	while(n>=0.5):
		count50+=1
		n = n-0.50
	while(n>=0.2):
		count20+=1
		n = n-0.20
	while (n>=0.10):
		count10+=1
		n = n-0.10
	while(n>=0.05):
		count5+=1
		n = n-0.05
	while(n>=0.02):
		count2+=1
		n = n-0.02
	while(n>=0.01):
		count1+=1
		n = n-0.01
	if(n!=0):
		count1+=1
	d[1] = count1
	d[2] = count2
	d[5] = count5
	d[10] = count10	
	d[20] = count20	
	d[50] = count50
	d[100] = count100
#	print(n)
	print(d)
def main():
	calculate_coins(0.11)
if __name__ == '__main__':
	main()