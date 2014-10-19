#python28.py
def count_words(arr):
    d = {}
    for word in arr:
        if word not in d:
            d[word] = 1
        else:
            d[word] +=1
    return d
    #print(d)
#def main():
#    count_words(["apple", "apple", "apple"])
#if __name__ == '__main__':
#    main()
                                      