#problem32.py
#import re
#5-1=4<
#i=0,i=1,i=2,i=3
#i=4
def is_an_bn(word):
    index = 0
    countA = 0
    countB = 0
    if(len(word)<1):
        return True
    while(word[index] == 'a' and index<len(word)-1):
        countA +=1
        index +=1
    while(word[index] == 'b' and index<len(word)-1):
        countB +=1
        index +=1
    if(word[index]=='b'):
        countB +=1
    #print(countA)
    #print(countB)
    if countA==countB:
        return True
    else:
        return False

#def main():
    #is_an_bn("")
#    print(is_an_bn("aabb"))
    #is_an_bn("aabbb")
    #is_an_bn("raabb")
#if __name__ == '__main__':
#    main()