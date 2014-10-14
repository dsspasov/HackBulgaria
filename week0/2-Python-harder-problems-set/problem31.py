#problem31.py
def prepare_meal(number):
    count3 = 0
    count5 = 0
    while(number%3==0):
        count3 +=1
        number = number//3
    while(number%5==0):
        count5 +=1
        number = number//5
    text =""
    if count3!=0:
        for x in range(count3):
            text +="spam "
        if count5!=0:
            text += "and "
            for x in range(count5):
                text +="eggs "
        return text
    else:
        if count5!=0:
            for x in range(count5):
                text +="eggs "
        return text
    return text


        #trqbva da se napravi da izvejda stringa
    #print (count3)
    #print (count5)
def main():
    print(prepare_meal(15))
if __name__ == '__main__':
    main()