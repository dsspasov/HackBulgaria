#cahs_desk.py
class CashDesk:
    def __init__(self):
        self.money = {100:0, 50:0, 20:0, 10:0, 5:0, 2:0, 1:0}
    def take_money(self,taken_money):
        for key in taken_money:
            self.money[key] = taken_money[key]
    def total(self):
        total = 0
        for key in self.money:
            total+=(key*self.money[key])
        return total
    def can_withdraw_money(self,amount_of_money):
        #from problem26.py calculate_coins(money)
        balance = self.total() - amount_of_money
        #print(balance)
        count100=0
        count50 =0
        count20 =0
        count10 =0
        count5 = 0
        count2 = 0
        count1 = 0
        di={}
        while(balance>=100):
            count100 +=1
            balance=balance-100
        while(balance>=50):
            count50+=1
            balance = balance-50
        while(balance>=20):
            count20+=1
            balance = balance-20
        while (balance>=10):
            count10+=1
            balance = balance-10
        while(balance>=5):
            count5+=1
            balance = balance-5
        while(balance>=2):
            count2+=1
            balance = balance-2
        while(balance>=1):
            count1+=1
            balance = balance-1
        di[1] = count1
        di[2] = count2
        di[5] = count5
        di[10] = count10 
        di[20] = count20 
        di[50] = count50
        di[100] = count100
        #print(di[1])
        #print( di ) 
        #print(self.money)
        for key in di:
            if di[key]!=0 and self.money[key] < di[key]:
                #print(di)
                return False
        return True
def main():
    my_cash_desk = CashDesk()
    my_cash_desk.take_money({1:2, 100:3})
    print(my_cash_desk.total()) # 72
    print(my_cash_desk.can_withdraw_money(100)) #False
    #print(my_cash_desk.can_withdraw_money(100)) #True

if __name__ == '__main__':
    main()