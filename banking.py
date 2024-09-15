class CreditCard:
    def __init__(self,customer,bank,acnt,limit):
        self.customer=customer
        self.bank=bank
        self.acnt=acnt
        self.limit=limit
        self.balance=0
    def get_customer(self):
         return self.customer
    def get_bank(self):
        return self.bank
    def get_acnt(self):
        return self.acnt
    def get_limit(self):
        return self.limit
    def get_balance(Self):
        return self.balance
    def charge(self,price):
        if price+self.balance>self.limit:
            return False
        else:
            self.balance += price
            return True

    def make_payment(self,amount):
        self.balance -= amount

if __name__ == '__main__':
    wallet=[]
    wallet.append(CreditCard('Agas','allinagaram','3243 3434 3423 2344','1000'))
    wallet.append(CreditCard('Agas','allinagaram','3243 3434 3423 2344','1000'))
    wallet.append(CreditCard('Agas','allinagaram','3243 3434 3423 2344','1000'))

    for val in range(1,17):
        wallet[0].charge(val)
        wallet[1].charge(2*val)
        wallet[2].charge(3*val)

    for c in range(3):
        print('Customer=',wallet[c].get_customer())
        print('Bank=',wallet[c].get_bank())
        print('Account=',wallet[c].get_acnt())
        print('Limit=',wallet[c].get_limit())
        print('Balance=',wallet[c].get_Balance())
        while wallet[c].get_balance()>100:
            wallet[c].make_payment(100)
            print('New balance=',wallet[c].get_Balance())
        print()
    
