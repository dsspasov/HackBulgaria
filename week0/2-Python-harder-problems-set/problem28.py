#python28.py
def count_words(arr):
    d = {}
    for word in arr:
        if word not in d:
            d[word] = arr.count(word)
    print(d)
def main():
    count_words(["apple", "banana", "apple", "pie"])
if __name__ == '__main__':
    main()
                                      