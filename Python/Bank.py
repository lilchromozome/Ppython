# -*- coding: utf-8 -*-
"""
Created on Wed Oct 19 13:07:40 2022

@author: willi
"""

class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
        self.history = []
        
    def getBalance(self):
        return self.balance
    
    def getOwner(self):
        return self.owner
    
    def __str__(self):
        return f'{self.getOwner()}\'s account contains ${self.getBalance():.02f} dollars'
    
    def withdraw(self, sub):
        self.balance -= sub
        self.history.append(self.balance)
        
    def deposit(self, add):
        self.balance += add
        self.history.append(self.balance)
        
    def transferTo(self, account, muny):
        self.withdraw(muny)
        account.deposit(muny)
        
    def getHistory(self):
        return self.history
    
class SavingsAccount(Account):
    def __init__(self, owner, balance, interestRate):
        Account.__init__(self, owner, balance)
        self.interestRate = interestRate
        
    def getInterestRate(self):
        return self.interestRate
    
    def addInterest(self):
        self.deposit(self.interestRate * 0.01 * self.balance)
        return self.balance
    
def main():
    m = SavingsAccount("Josh", 45, 10)
    n = Account("q", 5)
    m.withdraw(5)
    print(m)    
    m.transferTo(n, 10)
    print(m)
    print(n)
    m.addInterest()
    print(m.getHistory())
    print(m)
    
if __name__ == "__main__": main()
