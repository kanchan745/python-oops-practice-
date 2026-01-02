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


