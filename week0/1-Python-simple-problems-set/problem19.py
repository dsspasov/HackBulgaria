#problem19.py
from problem14 import number_to_list
from problem15 import list_to_number
def zero_insertion(n):
	x= number_to_list(n)
	u = []
	u.append(x[0])
	for i in range(len(x)-1):
		if x[i] == x[i+1]:
			#x.insert(i+1,0)
			u.append(0)
			u.append(x[i+1])

			#u.append[x[i+1]]
			print(x)
		elif (x[i]+x[i+1])%10 == 0:
			#x.insert(i+1,0)
			u.append(0)
			u.append(x[i+1])
		else:
			u.append(x[i+1])
	k = list_to_number(u)
	#print(k)
	return k

def main():
	#z=zero_insertion(5555)
	#print(z)
	print(zero_insertion(6446))
if __name__ == '__main__':
	main()

