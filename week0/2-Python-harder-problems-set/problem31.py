#problem31.py
def prepare_meal(number):
    count3 = 0
    count5 = 0
    while (number!=0 and number%3==0):
        count3 +=1
        number = number//3
    while(number!=0 and number%5==0):
        count5 +=1
        number = number//5
    text ="Empty"
    if count3!=0:
        text = ""
        for x in range(count3):
            text +="spam "
        if count5!=0:
            text += "and "
            for x in range(count5):
                text +="eggs "
        return text
    else:
        if count5!=0:
            text = ""
            for x in range(count5):
                text +="eggs "
        return text
    return text