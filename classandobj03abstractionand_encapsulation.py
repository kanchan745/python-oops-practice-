#Abstraction : Hiding the implementation detail of a class and only showing the essential feactures to the user..
#chhupahua(hidded)- unnessary , show : necessary 
#encapsulation : wrapping data and functions into a single unit (objects)
#ABSTRACTION , ENCAPSULATION , INHERITANCE , POLYMORPHISM


#Abstraction.....
# class  Car :
#     def __init__(self):
#         self.acc = False
#         self.brk = False
#         self.clutch = False
#     def start(self):
#         self.clutch = True 
#         self.acc = True
#         print("Car started.....")
        
# car1 = Car()
# car1.start()        

#Encapsulation : capsule : data + related function... in a single unit 
#all we coded that was encapsulation : wrapping data and function into a single unit (object)

#Pratice Ques 

class Account :
    def __init__(self, bal , acc):
        self.balance = bal 
        self.account_no = acc
        
     
    def debit (self, amount):
        self.balance -= amount
        print("Rs." , amount, "was debited..... ")  
        print("Total balance = ", self.get_balance()) 
        
    def credit (self, amount):
        self.balance += amount
        print("Rs." , amount, "was  credited") 
        print("Total balance = ", self.get_balance())
        
    def get_balance (self):
        return self.balance
           
acc1 = Account(100,1253)
acc1.debit(10)
acc1.credit(500000) 
          