# A = "aaabbbcccc"
# B = " "
# Count = 0
# for i in A:
#     if i in A:
#         A.append(i)
#     else:
#         Count += 0 
# print(A)

   
# A = 'Hello World'
# print(A[::-1])


# from abc import ABC,abstractmethod
# class Help4code(ABC):
#     @abstractmethod
#     def training(self):
#         pass
#     @abstractmethod
#     def placement(self):
#         pass
# class Ashish(Help4code):
#     def training(self):
#         print('C, C++, JAVA')
#     def placement(self):
#         print('Java placement')
# class Ankush(Help4code):
#     def training(self):
#         print("Python  |   Django")
#     def placement(self):
#         print('Python Placement students')
# class Prashant(Help4code):
#     def training(self):
#         print('Machin Learning') 
#     def placement(self):
#         print("Data Science PLacement")
# obj1 = Ashish()
# obj1.training()
# obj1.placement()

# obj2 = Ankush()
# obj2.training()
# obj2.placement()

# obj3 = Prashant()
# obj3.training()


# from abc import ABC,abstractmethod
# class Irctc(ABC):
#     @abstractmethod
#     def bookTicket(self):
#         pass
# class MakeMyTrip(Irctc):
#     def bookTicket(self):
#         print('==========================================')
#         print('          WELCOME TO makemytrip.com       ')
#         source  = input("Enter a sorce station name")
#         destination = input("Enter destination")
#         date = input("Enter date")
#         print('==========================================')
        
# class GoIbibo(Irctc):
#     def bookTicket(self):
#         print('          WELCOME TO GOTBIBO      ')
#         source  = input("Enter a sorce station name")
#         destination = input("Enter destination")
#         date = input("Enter date")
        
# class Yatra(Irctc):
#     def bookTicket(self):
#         print('          WELCOME TO YATRA     ')
#         source  = input("Enter a sorce station name")
#         destination = input("Enter destination")
#         date = input("Enter date")
        
# m = MakeMyTrip()  
# m.bookTicket()  
# g = GoIbibo()  
# g.bookTicket()  
# y = Yatra()  
# y.bookTicket() 


# class Base:#parent class
#     def __init__(self):
#         print('Parent class constructor called')
#         self.a = 'khushi'#public data member
#         self.__c = "Disha"#private member
# class Derived(Base):#child class
#     def __init__(self):
#         #calling constructor of Base class
#         Base.__init__(self)
#         # print("Calling private member of base class")
#         # print(self.a)
#         # print(self.__c)
# # obj1 = Derived()
# # print(obj1.a)
# # print(obj1.__c)
# obj2 = Base()
# print(obj2.a)#Accesible
# print(obj2.__c)#not accesible

# class Rbi:
#     #declaring then public method
#     def publicPolicy(self):
#         print("Check the public policy of RBI")
        
#         #declaring private method
#     def __privatePolicy(self):
#         print("There is some private policy which is not accesible for public")
        
# class Sbi(Rbi):
#     def __init__(self):#1st sbi class const called
#         Rbi.__init__(self)#2nd parent class constr called
#     def callingPublicMethod(self):#child class public method
#         print("\nInside child class")
#         self.publicPolicy()#calling parent class public method
#     def callingPrivateMethod(self):#child class public method
#         self.__privatePolicy()#calling parent class private method
# obj1 = Sbi()
# obj1.callingPublicMethod()
# obj1.callingPrivateMethod()
# obj1.publicPolicy()
# obj1.__privatePolicy()

# obj2 = Rbi()
# obj2.publicPolicy()
# obj2.__privatePolicy()

# obj2 = Rbi()
# obj2.publicPolicy()
# obj2._Rbi__privatePolicy()

# A = [10, 98, 3, 33, 12, 22, 21, 11]
# B = [ ]
# C = [ ]
# for i in A:
#     if i%2 :
#         # A.sort()
#         B.append(i)
#     elif i !=B: 
#         C.append(i)
#     else:
#         pass
# print(A)
# print(C + B)
# print(B)
        
# ================================================
# Data Structure
# ================================================
# import sys
# class Stack:
#     def __init__(self):
#         self.stackList = []#stack created
        
#     def push(self,value):
#         self.stackList.append(value)
#     def displayStack(self):
#         print('=========================')
#         print(self.stackList)
#         print('=========================')
#     def isEmpty(self):
#         if self.stackList == []:
#             return True
#         else:
#             return False
#     def pop(self):
#         if self.isEmpty():
#             return "Stack is Empty"  
#         else:
#             self.stackList.pop()
#     def delete(self):
#         self.stackList = None 
#         return "Delete stCK"
#     def peek(self):
#         if self.isEmpty():
#             return "Stack is empty"
#         else:
#             return self.stackList[-1]
# stackObj = Stack()
        
# while True:
#     print("1.Push Element in stack:")
#     print("2.Display Stack elements:")
#     print("3.check is Empty")
#     print("4.Pop operation in Stack :")
#     print('5.Delete stack')
#     print('6.Show Top Element from stack')
#     print('7.Exit')
#     choice = int(input('Enter your choice :'))
#     if choice == 1:
#         val = int(input('Enter the value for stack:'))
#         stackObj.push(val)
#     elif choice ==2:
#         stackObj.displayStack()
#     elif choice == 3:
#         print(stackObj .isEmpty())
#     elif choice==4:
#         print(stackObj.pop())
#     elif choice == 5:
#         print(stackObj.deleteStack)
#     elif choice == 6:
#         print(stackObj.peek())
#     elif choice == 71:
#         sys.exit()

# ===========================================================    
# without with size limit
# =============================================================
# import sys
# class Stack:
#     def __init__(self, stackSize):#parameterize constructor
#         self.stackList = []#stack created
#         self.stackSize = stackSize
        
#     def isFull(self):
#         if len(self.stackList) == self.stackSize:
#             return True
#         else:
#             return False
        
#     def push(self,value):
#         if self.isFull():
#             print('Stack is full')
#         else:
#             self.stackList.append(value)
#     def displayStack(self):
#         print('=========================')
#         print(self.stackList)
#         print('=========================')
#     def isEmpty(self):
#         if self.stackList == []:
#             return True
#         else:
#             return False
#     def pop(self):
#         if self.isEmpty():
#             return "Stack is Empty"  
#         else:
#             self.stackList.pop()
#     def delete(self):
#         self.stackList = None 
#         return "Delete stCK"
#     def peek(self):
#         if self.isEmpty():
#             return "Stack is empty"
#         else:
#             return self.stackList[-1]

# size = int(input('Enter the size of stack'))
# stackObj = Stack(size)#stack object has created
        
# while True:
#     print("1.Push Element in stack:")
#     print("2.Display Stack elements:")
#     print("3.check is Empty")
#     print("4.Pop operation in Stack :")
#     print('5.Delete stack')
#     print('6.Show Top Element from stack')
#     print('7.Exit')
#     choice = int(input('Enter your choice :'))
#     if choice == 1:
#         val = int(input('Enter the value for stack:'))
#         stackObj.push(val)
#     elif choice ==2:
#         stackObj.displayStack()
#     elif choice == 3:
#         print(stackObj .isEmpty())
#     elif choice==4:
#         print(stackObj.pop())
#     elif choice == 5:
#         print(stackObj.deleteStack)
#     elif choice == 6:
#         print(stackObj.peek())
#     elif choice == 71:
#         sys.exit()


#Tower of Hanoi:
# import time
# class Tower:
    
#     def __init__(self):
#         print("WELCOME TO TOWER OF HONOI GAME")
#         print()
#         print("Problem : A[1,2,3]       B[]       C[]")
#         print()
#         print("Goal :    A[]            B[]       C[1,2,3]")
#         self.A = []
#         self.B = []
#         self.C = []

#     def tower(self,item):
#         self.A.append(item)
#         time.sleep(3)
#         print("A = ",self.A)
#         print("Items in Tower A\n")

#     def pass1(self):
#         self.temp = self.A.pop(2)
#         self.C.append(self.temp)
#         time.sleep(3)
#         print("A = ",self.A     ,"     ",    "B = ",self.B      ,"     ", "C = ",self.C)
#         print("Pass 1 Complete =====================================")

#     def pass2(self):
#         self.temp = self.A.pop(1)
#         self.B.append(self.temp)
#         time.sleep(3)
#         print("A = ",self.A     ,"     ",    "B = ",self.B      ,"     ", "C = ",self.C)
#         print("Pass 2 Complete =====================================")
    
#     def pass3(self):
#         self.temp = self.C.pop(0)
#         self.B.append(self.temp)
#         time.sleep(3)
#         print("A = ",self.A     ,"     ",    "B = ",self.B      ,"     ", "C = ",self.C)
#         print("Pass 3 Complete =====================================")
    
    
#     def pass4(self):
#         self.temp = self.A.pop(0)
#         self.C.append(self.temp)
#         time.sleep(3)
#         print("A = ",self.A     ,"     ",    "B = ",self.B      ,"     ", "C = ",self.C)
#         print("Pass 4 Complete =====================================")

#     def pass5(self):
#         self.temp = self.B.pop(0)
#         self.A.append(self.temp)
#         time.sleep(3)
#         print("A = ",self.A     ,"     ",    "B = ",self.B      ,"     ", "C = ",self.C)
#         print("Pass 5 Complete =====================================")
    
#     def pass6(self):
#         self.temp = self.B.pop(0)
#         self.C.append(self.temp)
#         time.sleep(3)
#         print("A = ",self.A     ,"     ",    "B = ",self.B      ,"     ", "C = ",self.C)
#         print("Pass 6 Complete =====================================")
    
#     def pass7(self):
#         self.temp = self.A.pop(0)
#         self.C.append(self.temp)
#         time.sleep(3)
#         print("A = ",self.A     ,"     ",    "B = ",self.B      ,"     ", "C = ",self.C)
#         print("Pass 7 Complete =====================================")

    

# obj1 = Tower()
# obj1.tower(3)
# obj1.tower(2)
# obj1.tower(1)
# obj1.pass1()
# obj1.pass2()
# obj1.pass3()
# obj1.pass4()
# obj1.pass5()
# obj1.pass6()
# obj1.pass7()




