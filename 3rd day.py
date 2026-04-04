# mydict = {
#     101:"khushi",
#     102:"pooja",
#     "103" : "tanvi",
#     "104" : " disha",
#     101 : "pooja",
#     104 : "pooja"
# }
# print(mydict)

#with the help of key we have to print values
# a = mydict[102]
# print(a)

# mydict[102] = "peter"
# print(mydict) #{101: 'pooja', 102: 'peter', '103': 'tanvi', '104': ' disha', 104: 'pooja'}
# only print key x=0,1
# for x in mydict:
#     print(x)

# only print value x = 0
# for x in mydict.values():
#     print(x)

# printing key and values both
# for x,y in mydict.items():
    # print(x,y)
    
# if you have to add new key and value pair in my dictionary
# mydict["mobile_no"] = 4646463738
# print(mydict)

# a = {(1,2):1,(2,3):2,(4,5):3}
# print(a[4,5])

# a = {'a':1,'b':2,'c':3}
# print(a['a','b'])

# arr = {}
# arr[1] = 1
# arr['1'] = 2
# arr[1] += 1
# sum = 0
# for k in arr:
#     sum += arr[k]
# print(sum)#4

# mydict = {}
# mydict[1] = 1
# mydict['1'] = 2
# mydict[1.0] = 4
# print(mydict)
# sum =0
# for k in mydict:
#     sum += mydict[k]
# print(sum) #6

# box = {}
# jars = {}
# crates = {}
# box['biscuit'] = 1
# box['cake'] = 3
# jars['jam'] = 4
# crates['box'] = box
# crates['jars'] = jars
# print(len(crates[box])) #TypeError: unhashable type: 'dict'

# dict = {'c':97,'a':96,'b':98}
# for _ in sorted(dict):
#     print(dict[_]) #96 98 97

# rec = {"name" : "python" ,"age":"20"}
# r = rec.copy()
# print(id(r) == id(rec)) #False
# print(id(r)) #1555005569664
# print(id(rec)) #1555005350912

# rec = {"name" : "python","age":"20","addr":"NJ","country":"USA"}
# id1 = id(rec)
# del rec
# print(id(id1))
# rec = {"Name" : "python","age":"20","addr":"NJ","country":"USA"}
# id2 = id(rec)
# print(id(id2))
# print(id1 == id2)

# def find_min_key(d):
#     min_key = None
#     min_value = float('inf')  # start with a very large number
    
#     for key in d:
#         if d[key] < min_value:
#             min_value = d[key]
#             min_key = key
            
#     return min_key

# # Input
# my_dict = {"X": 20, "Y": 10, "Z": 30}


# mydict ={
#     101:"khushi",
#     "professional" : "developer",
#     "empid": 1001
# }
# mydict.pop(101)
# print(mydict)
# # pop()method remove pair by specific key name

# Nested for loop
# (i,j)=(1,1)
# for i in range(1,4):
#     for j in range(1,4):
#       print(i, end=" ")
#     print()

# n = (int(input("enter the number of rows:")))
# for i in range(1,n+1):
#     for j in range(1,1+i):
#         print(j,end=" ")
#     print()

# n = int(input("enter the number of rows"))
# for i in range(1,n+1):
#     for j in range(1,1+i):
#         print(chr(64+i),end=" ")
#     print()
    
# n = int(input("enter the number of rows"))
# for i in range(1,n+1):
#     for j in range(1,n+2-i):
#         print("*",end=" ")
#     print()

# n = int(input("enter the number of rows"))
# for i in range(1,n+1):
#     for j in range(1,n+2-i):
#         print(chr(64+j),end=" ")
#     print()

# import time
# n = int(input("enter the number of rows"))
# for i in range(1,n+1):
#     for j in range(1,n+2-i):
#         time.sleep(2)
#         print(n+1-i,end="  ")
#     print()

# import time
# n = int(input("enter the number of rows"))
# for i in range(1,n+1):
#     print(" "*(n-i),end=" ")
#     for j in range(1,i+1):
#         time.sleep(2)
#         print("*",end=" ")
#     print()

# Function in python
# def msg(): #called function
#     print("Hello World")

# msg()#calling function
# msg()

# def arithmetic():
#     a = int(input("Enter the value of A: "))
#     b = int(input("Enter the value of B: "))
#     add = a+b
#     sub = a-b
#     mul = a*b
#     div = a/b
#     return add,sub,mul,div
# print(arithmetic())#calling function 
# Enter the value of A: 10
# Enter the value of B: 2
# (12, 8, 20, 5.0)    # 

# def arithmetic():
#     a = int(input("Enter the value of A: "))
#     b = int(input("Enter the value of B: "))
#     add = a+b
#     sub = a-b
#     mul = a*b
#     div = a/b
#     return add,sub,mul,div
# result = arithmetic()
# print("Arithmetic = ",result)
# print(arithmetic())
# Enter the value of A: 5
# Enter the value of B: 4
# Arithmetic =  (9, 1, 20, 1.25)
    
# Positional
# def login(username,password):
#     if username == password:
#         print('login succesful')
#     else:
#         print("Invalid credntial")
# username = input("Enter the username: ")
# password = input("enter the password: ")
# login(username,password)

#Keyword
# def login(username,password):
#     if username == password:
#         print('login succesful')
#     else:
#         print("Invalid credntial")
# login(username="admin",password = "admin")

# default
# def cityName(city="Goa"):
#     print(city)
# cityName("Sawantwadi")
# cityName("Nagpur")
# cityName()

# variable length argument/variable number of arguments
# def nameofCity(*city):
#     print("city Name's = ",city)
# nameofCity("goa","Nagpur","pune","mumbai","Nashik")

# WAP for menu driven code
# import sys
# def add():
#     val1 = int(input("Enter the value of val1 : "))
#     val2 = int(input("Enter the value of val2 : "))
#     print("Add =",val1+val2)
# def sub():
#     val1 = int(input("Enter the value of val1 : "))
#     val2 = int(input("Enter the value of val2 : "))
#     print("Sub =",val1-val2)
# def mul():
#     val1 = int(input("Enter the value of val1 : "))
#     val2 = int(input("Enter the value of val2 : "))
#     print("Mul =",val1*val2)
# def div():
#     val1 = int(input("Enter the value of val1 : "))
#     val2 = int(input("Enter the value of val2 : "))
#     print("Div =",val1/val2)

# while True:
#     print("1.Addition")
#     print("2.Subtraction")
#     print("3.Multiplication")
#     print("4.Division")
#     print("5.Exit")
#     choice = int(input("Enter your choice"))
#     if choice == 1:
#         add()
#     elif choice == 2:
#         sub()
#     elif choice == 3:
#         mul()
#     elif choice == 4:
#         div()
#     elif choice == 5:
#         sys.exit()

# 1. rstrip() ==> to remove spaces at right hand side
# 2. lstrip() ==> to remove spaces at left hand side
# 3. strip() ==> to remove spaces at both side
# programming = input("Enter your programming Name: ")
# p_name = programming.rstrip()
# if p_name == 'Python':
#     print(p_name)
# elif p_name == 'Java':
#     print(p_name)
# elif p_name == 'CPP':
#     print(p_name)
# else:
#     print("Wrong programing name")
        