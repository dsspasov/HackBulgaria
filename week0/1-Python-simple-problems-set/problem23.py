#problem23.py
def nan_expand(times):
	text= ""
	if(times==0):
		return text
	else:
		for x in range(times):
			text = text + "Not a "
	text = text + "NaN"
	return text
def main():
	print (nan_expand(2))
if __name__ == '__main__':
	main()