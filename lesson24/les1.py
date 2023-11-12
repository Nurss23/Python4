class Counting:
    def __init__(self,bal):
        self.balance = 0
    def coming(self,num):
        self.balance += num
        print(self.balance)
    def care(self,num):
        return(self.balance - num)
    
num = Counting
num.coming(150)
print(num.care(50))