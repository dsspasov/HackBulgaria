#problem30.py
def groupby(func, seq):
    d={}
    if not seq:
        d={'odd':0,'even':0}
    else:
        for x in seq:
            if func(x) not in d:
                d[func(x)] = [x]
            else:
                d[func(x)].append(x)
    return d
    #print(d)
#def main():
#    groupby(lambda x: 'odd' if x % 2 else 'even', [1, 2, 3, 5, 8, 9, 10, 12])
#if __name__ == '__main__':
#    main()