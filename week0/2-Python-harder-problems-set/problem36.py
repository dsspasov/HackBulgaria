#problem36.py
def nth_fib_lists(listA, listB, n):
    if n==1:
        return listA
    if n==2:
        return listB
    if n==3:
        return listA+listB
    else:
        return nth_fib_lists(listA,listB,n-1)+nth_fib_lists(listA,listB,n-2)