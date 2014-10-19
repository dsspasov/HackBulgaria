#problem37.py
from problem36 import nth_fib_lists
def member_of_nth_fib_lists(listA, listB, needle):
    i=1
    while (len(needle)>=len(nth_fib_lists(listA,listB,i))):
        #print(nth_fib_lists(listA,listB,i))
        if needle == nth_fib_lists(listA,listB,i):
            return True
        i+=1
    else:
        return False
#def main():
#    print( member_of_nth_fib_lists([7,11], [2], [11,7,2,2,7]) )
#if __name__ == '__main__':
#    main()
