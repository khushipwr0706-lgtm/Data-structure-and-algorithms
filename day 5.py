# A = [1,2,3,4,5]
# A. reverse()
# print(A)

# 2nd logic
# A = [1,2,3,4,5]
# print(A[::-1])


# A = [1,2,3,2,1]
# print(A)
# print(A[::-1])
# if A == A[::-1]:
#     print("This is palindrome")
# else:
#     print("Not a polindrome")

# A = [1,2,3,2,4,5]
# B = []
# C = []
# for i in A:
#     if i not in  B:
#         B.append(i)
#     elif i not in C:
#         C.append(i)
#     else:
#         pass
# print(B)
# print(C)

# class and object
# class Student:
#     roll_no = 101
    
#     def studentdata(self):
#         print("Student Information")
        
# obj = Student()
# print(obj.roll_no)
# obj.studentdata()


# class Demo:
#     def __init__(self):
#         print("I am constructor")
#     def msg(self):
#         print("Hello class!")
# obj1 = Demo()#I am constructor

# class Demo:
#     def __init__(self):
#         print("I am constructor")
#     def msg(self):
#         print("Hello class!")
# obj1 = Demo()
# # print(obj1) #<__main__.Demo object at 0x000002666AC88980>
# obj2 = Demo()
# obj1.msg()

# class Hod:
#     def __init__(self):
#         self.name='Khushi pawar'
#         self.age = 22
#         self.empid = 1001
#     def info(self):
#         print("My name is :",self.name)
#         print("My age is :",self.age)
#         print("My emp id id ",self,self.empid)
# obj = Hod()
# obj.info()
# ---------------------------------------------------------------------
# op
# My name is : Khushi pawar
# My age is : 22
# My emp id id  <__main__.Hod object at 0x000001D6AFA28980> 1001


# class Hod:
#     def __init__(self,name,age,roll_no):
#         self.name = name
#         self.age = age
#         self.roll_no = roll_no
#     def show(self):
#         print("name = ",self.name)
#         print('age = ',self.age)
#         print('roll_no =',self.roll_no)
# obj = Hod('Khushi',43,101)
# obj.show()

# -----------------------------------------------------------------
# 10
# 10
# 10

# 20
# 10
# 10
# ---------------------------------------------------------------

# declaring instance variable outside a class by using object
# class Student:
#     def __init__(self):
#         self.s_name = "Khushi"
#         self.s_rollno = 101#declaring a instance var inside a constructor
#     def getdata(self):
#         self.s_mb = 28282828282#declaring a instance var inside a instance method
# obj = Student()
# obj.getdata()
# del obj.s_mb
# obj.s_branch = 'CS'#delete the instance variable using obj
# print(obj.__dict__)#adding instance variable by using object
# -----------------------------------------------------------
# {'s_name': 'Khushi', 's_rollno': 101, 's_branch': 'CS'}
# --------------------------------------------------------

# class New():
#     a =10
    
#     def __init__(self):
#         self.name = 'Khushi'
# obj1 = New()
# obj2 = New()
# obj3 = New()
# print(obj1.a)
# print(obj2.a)
# print(obj3.a)
# New.a = 50
# print(obj1.a)
# print(obj2.a)
# print(obj3.a)

# class Student():
#     def __init__(self):
#         print("Student Management System")
#         self.studentID = []
#         self.studentName = []
#         self.studentRollno = []
#         self.studentCity = []
#     def addStudent(self):
#         self.studentID.append(input("Enter the student ID: "))
#         self.studentName.append(input("Enter the student Name: "))
#         self.studentRollno.append(input("Enter the student Roll no: "))
#         self.studentCity.append(input("Enter the student City: "))       
        
# obj1 = Student()
# obj1.addStudent()
# obj2 = Student()
# obj2.getdata()

# instance method
# class Student():
#     def __init__(self, name, rollno, mob):
#         self.name = name
#         self.rollno = rollno
#         self.mob = mob
#     def display(self):
#         print(self.name," ",self.rollno," ",self.mob)
# stud = Student("khushi",1001,6789263571)
# stud.display()

# Static method
# class Student:
#     @staticmethod
#     def get_personal_detail(firstname,lastname):
#         print('your personal detail = ',firstname,lastname)
        
#     @staticmethod
#     def contact_detail(mobile_no, rollno):
#         print('your contact detail = ',mobile_no,rollno)
        
# Student.get_personal_detail('khushi','pawar')
# Student.contact_detail(9127654276 , 1002)
#  ----------------------------------------------------------------------       
# Inheritance in python
# single inheritance
# class College:#parent class
#     def college_name(self):#member function of college
#         print('YBIT College')
# class Student(College):#child class
#     def student_info(self):#member function
#         print('Name:  khushi pawar')
#         print("Branch:  CS")

# obj =Student()#object create child class
# obj.college_name()
# obj.student_info()

# -----------------------------------------------
# Mulilevel inheritance
# class College:
#     def college_name(self):
#         print('YBIT College')
# class Student(College):
#     def student_info(self):
#         print('Name:  Khushi Pawar')
#         print('Branch:  CSE')
# class Exam(Student):
#     def subject(self):
#         print('Subject1: Design Engineering')
#         print('Subject2: DBMS')
#         print('Subject3: C-Language')
# obj =Exam()
# obj.college_name()
# obj.student_info()
# obj.subject()

# class SubjMarks: # class-1  
#   math = int(input("Enter paper marks of math :"))  
#   DE = int(input("Enter paper marks of design engineering :"))  
#   c = int(input("Enter paper marks of c language :"))  
#   english = int(input("Enter paper marks of English :"))  
#================================= parent class -1  
# class PractMarks: # class-   
#   cpract = int(input("Enter practicals marks of c language :"))    
#================================= parent class -2  
# class Result(SubjMarks,PractMarks): # child class  
  #print("if student pass in both = subject and practical paper then pass")  
#   def total(self):  
    # if self.math>=40 and self.DE>=40 and self.c>=40 and self.english>=40 and self.cpract>=20:  
    #   print("pass")  
    # else:  
    #   print("fail")  
# obj = Result()  
# obj.total()  

#polymorphism
# class Principle:
#     def role(self):
#         print("I am managing all activity of college")
# class Dean:
#     def role(self):
#         print('Dean = i am decision taking person')
# class Hod:
#     def role(self):
#         print('Hod = I have responsibility of Teachers and Students')
# class Faculty:
#     def role(self):
#         print('Faculty = i have to complete syllabus successfully')
# def func(obj):#called function obj = 1.Dean
#     obj.role()#calling func
# campus=[Principle(),Dean(),Faculty()]
# for obj in campus:#obj =[0:Principle(),1:Dean.2]:Hod
#     func(obj)#calling fun

# class Arithmetic:
#     def add(self,a = None,b = None,c=None):
#         if a != None and b != None:
#             print(a+b)
#         elif a!=None and b!=None and c!=None:
#             print(a+b+c)
#         else:
#             print('enter atleast two arguments')
# obj =  Arithmetic()
# obj.add(10)
# obj.add(10,20)
# obj.add(1,2,3)

# Constructor overloading
#constructor overloading not possible in python
# if we define multiple constructor then the last constructor will be
# class Arithmatic:  
#     def __init__(self):  
#         print("There is no argument")  
#     def __init__(self,a):  
#         print("passing one argument")  
#     def __init__(self,a,b):  
#         print("passing two arguments")  
  
# obj = Arithmatic()  
# obj = Arithmatic(10)  
# obj = Arithmatic(2,2)  

# python supports overriding supports 
# method overriding(parent and child relationship must be there)
# class Rbi:
#     def home_loan(self):
#         print('Home LOan = 7.5')
#     def car_loan(self):
#         print('Car Loan 8%')
# class Sbi(Rbi):
#     def home_loan(self):
#         print("Sbi Provide home loan = 6.5")
# obj = Sbi()
# obj.home_loan()

# class Rbi:
#     def home_loan(self):
#         print('Home LOan = 7.5')
#     def car_loan(self):
#         print('Car Loan 8%')
# class Sbi(Rbi):
#     def home_loan(self):
#         print("Sbi Provide home loan = 6.5")
#         super().home_loan()#using super()you can access the method from parent class into child class 
# obj = Sbi()
# obj.home_loan()

class Father:
    def __init__(self):
        print('Father:= i am already at breakfast table')
class Child(Father):
    def __init__(self):
        print('Child:= i will be late for breakfast ')#Child:= i will be late for breakfast
        super().__init__()
obj = Child()