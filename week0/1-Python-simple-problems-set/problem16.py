#problem16.py
def biggest_differnce(arr):
    current = big = 0
    for x in range(len(arr)-1):
        for y in arr:
            if arr[x] - y < current:
                current = arr[x] - y
            elif y-arr[x] <current:
                current = y-arr[x]
        if big>current:
            big = current
    return big
def main():
    f=  biggest_differnce(range(100))
    print(f)
if __name__ == '__main__':
    main()