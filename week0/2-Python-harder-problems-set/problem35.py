#problem35.py
def sort_fractions(fractions):
    #sorted_fractions = []
    new_list = []
    for x in fractions:
        new_list.append(x[0]/x[1])

    for i in range(len(fractions)-1):
        k = i
        for j in range(i,len(fractions)):
            if new_list[k] > new_list[j]:
                k=j

        x = new_list[k]
        new_list[k]= new_list[i]
        new_list[i] = x

        pom = fractions [k]
        fractions[k] = fractions[i]
        fractions[i] = pom

    return fractions

    #return sorted_fractions
#def main():
#    print(sort_fractions([(5, 6), (22, 78), (22, 7), (7, 8), (9, 6), (15, 32)]))
#if __name__ == '__main__':
#    main()
