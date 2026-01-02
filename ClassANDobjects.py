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

            
        
        
        
        
            
        
        
