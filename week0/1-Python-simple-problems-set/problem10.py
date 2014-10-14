#problem10.py
"""
ls -vijdam vsi4ki papki
hack izbiram nqkoq papki

	compiliram python3 problem10.py
"""
from problem9 import mklist

def is_number_balanced(n):
	if n<10:
		return True
	else:
		sum1=0
		sum2=0
		a = []
		a =mklist(n)
		l = len(a)
		for x in range(0,l//2):
			sum1=sum1+a[x]
		c = a[::-1]
		for y in range(0,l//2):
			sum2+=c[y]
		if sum1==sum2:
			return True
		else:
			return False
def main():
	b = is_number_balanced(28471)
	if (b):
		print("true")
	else:
		print("False")

if __name__ == '__main__':
	main()