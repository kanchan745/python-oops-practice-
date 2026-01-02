#class is a blueprint for creating objects 

#or we write information and feactures in class and we create objects from that class

'''class Student:#class keyword and class name capital letter
    name = "Karan"
#creating objects (instances) 
s1 = Student() #obj name = class name and parenthesis
print(s1.name) 
print(s1)  '''


# class Car :
#     colour = "Blue"
#     brand = "Mercedes"
# car1 = Car()
# print(car1.colour)  
# print(car1.brand)  

'''Constructor'''#special function called it __init__ function or constructor it ll invoke on the creation of obj
#execute on the time of  obj creation 
'''all the classes have fun called __init__() which is always executed when the obj is being initiated''' 
#always run without writing or writing a constructor 

# class Student:
#     def __init__(self):#constructor always take an argumnent which is called as self
#         #self means new obj which we created, or it is reference for that object 
#         print(self)
#         print("Adding new student in DataBASE...")  
# s1 = Student()
# #here we use parenthesis for construction calling
# print(s1)    

# class Student:
#     def __init__(self,fullname):
#         self.name = fullname
#         print("Adding a new student in database....")

# s1 = Student("kanchan")
# print(s1.name)        

'''class Student:
    def __init__(abcd, name):
        abcd.fullname =  name #that data we re storing is called as attributes
        print("The constructor calling for new object..")

s1 = Student("Kashish")
print(s1.fullname)  
s2 = Student("Arjun")
print(s2.fullname)  '''
#we can write self and any other name 
#the data is stored inside the variable is called attribute
#variable = attributes 
''' The self parameter is a reference to the current instance of the class , and is used to access variables that belong to the class'''

# class Student:
#     def __init__(self,name , marks, age):
#         self.name = name 
#         self.marks = marks 
#         self.age = age
#         print("constructor is calling for new obj.")
# s1 = Student("kanchan",97,21)
# print(s1.name,s1.marks,s1.age)
# s2 = Student("Kashish",96,22)
# print(s2.name)
# print(s2.marks)
# print(s2.age)

#constructor type default 

# class Ad:
#     def __init__(self):
#         print('calling a default constructor') #if we don't make by default python will make
#     def __init__(self,name):
#         self.name = name 
#         print('calling a parameterized constructor')

# s2 = Ad("card")
# print(s2.name)


'''Class and Instance attributes'''
#class attributes = common for all objects
#Instance attributes = different for all objects ex : name 
'''and instance object defined by self . '''#self is obj reference 
#college name : class attributes : obj occupy space in the memory so we don't store common for all
#common for all objects called class attribute      

# class Student :
#     college_name = '''Sirt College'''# it ll store only one time in memory because it is not with self 
#     def __init__(self, name ,Branch):
#         self.name = name 
#         self.branch = Branch
# s = Student("Kanchan", "Aiml")
# print(s.college_name)
# #one more way to access class attribute 
# print(Student.college_name)
# print(s.name, s.branch) 
#class attribute take one time memory only
#class.att , obj.attribute   

# class Student :
#    college_name = "SIRT college"
#    name = "anoymous" #class attributes
#    def __init__(self, name ):
#        self.name = name # obj attr> class attr
       
# s1 = Student ("Kanchan")
# print(s1.name)  

#class can store -> data and methods.
#data = attributes, properties , methods = how to work 
#class - inside function are called methods

#methods are functions that belong to objects 

# class Student:
#     def __init__(self , name , Branch):#constructor
        
#         self.name = name 
#         self.branch = Branch 
    
#     def welcome(self):
#         print("Welcome student!", self.name)
# s1 = Student("Kanchan", "aiml")
# print(s1.name , s1.branch)
# s1.welcome ()            

# class Student:
#     def __init__(self,name , marks): # constructor is used for object initiallization : object create karte time kuch karna hai to
        
#         self.name = name 
#         self.marks = marks
#     def welcome(self):
#         print("welcome", self.name )
        
#     def get_marks (self):
#         return self.marks    
    
# s1 = Student("kanchan", 99)
# s1.welcome()
# print(s1.get_marks())  
        
        
# class Student :
#     def __init__(self, name , marks_):
#         self.name = name 
#         self.marks = marks_
#     def avg(self):
#         sum = 0
#         for i in self.marks:
#             sum +=i
#         print("hii", self.name ,"Your avg marks is :", sum//3)
               
        
# s1 = Student("kanchan",[99,98,97])
# s1.avg()  
# s1.name = "kashish" # attribute val change possible
# s1.avg()      
     

# class Stu :
#     def __init__(self, name , marks):
#         self.name = name 
#         self.marks = marks
        
#     def avg(self):
#         sum = 0
#         for i in self.marks :   
#             sum += i
#         print("avg is : ", sum// len(self.marks))      
            
# s1 = Stu("kanchan", [99,98,97])
# s1.avg()            

# s1.name = "kashish"
# s1.avg()            

'''Static methods'''

#methods that don't use the self parameter(work at class level) we don't use self as it is not at obj level
#@staticmethod it convert to be a static method - decorator


#Dectorators allow us to wrap another function in order to extend the behaviour of the  wrapped function , without permanently modifying it 

# class Student :
#     def __init__(self, name , marks):
#         self.name = name 
#         self.marks = marks
    
#     @staticmethod
#     def hello():
#         print("Hello") 
        
# s1 = Student ("kanchan", 95)
# s1.hello() 
# print(s1.name, s1.marks,s1.hello())      

# a function which is decorator which take input (function) give output(function)    


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
          

            
        
        
        
        
            
        
        
