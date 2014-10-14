#problem29.py
def unique_words_count(arr):
    new_arr = []
    for word in arr:
        if word not in new_arr:
            new_arr.append(word)
    print(len(new_arr))
    #print(count)
    #print (len(new_arr))
def main():
    unique_words_count(["apple", "banana","banana", "apple", "pie"])
if __name__ == '__main__':
    main()