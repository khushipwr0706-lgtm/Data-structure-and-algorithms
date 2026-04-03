# name = "khushipawar"
# indexing = 012345678910
# print(name[0])
# print(name[1])
# print(name[-1])
# print(name[15])
# print(name[0:5])
# print(name[1:])
# print(name[:5])
# print(name[:])
# print(name[1:8:2])
# print(name[::-1])
# print(name[::4])

# s = "Python is a High level programming language"
# print (s.lower()) # python is a high level programming language
# print (s.upper()) # PYTHON IS A HIGH LEVEL PROGRAMMING LANGUAGE
# print (s.swapcase())# pYTHON IS A hIGH LEVEL PROGRAMMING LANGUAGE
# print (s.title())# Python Is A High Level Programming Language
# print (s.capitalize())# Python is a high level programming language

# print("Subject Marks")
# phy = 50
# chem = 60
# maths = 70
# print("physics = {} chemistry = {} math = {}".format(phy,chem,maths))
# print("physics = {0} chemistry = {1} math = {2}".format(phy,chem,maths))
# print("physics = {x} chemistry = {y} math = {z}".format(x=phy,y=chem,z=maths))
# total = phy+chem+maths
# print("Total marks",f"{total}")
# print("roll no =","7" . zfill(4))

# for (initalization:condition+:in/dec)
# for i in range(1,11):
#     print(i*2)

# for i in range(1,11):
#     print(i*2 ," ",i*3," ",i*4," ",i*5," ",i*6," ",i*7," ",i*8," ",i*9," ",i*10)
#     print()
    
# for i in range(1,11):
#     print(i*11 ," ",i*12," ",i*13," ",i*14," ",i*15," ",i*16," ",i*17," ",i*18," ",i*19," ",i*20)
#     print()
    
# name = "racear"
# for i in name:
#     print(i)
    
#  WAP to remove duplicates
# name = "racear"
# newname = ""
# for i in name:
#     if i not in newname:
#         newname +=i
# print(name)
# print(newname)

# for i in range(5,0,-1):
#     print(i)

# for i in range(10,0,-2):
#     print(i)
    
# name="Mumbai"
# newname=""
# n = len(name)
# for i in range(n-1,-1,-1):
#     newname += name[i]
# print(name)
# print(newname)
    
# name = "ama"
# print(name)
# print(name[::-1])

# if name == name[::-1]:
#     print("palindrome string")
# else:
#     print("It is not palindrome")
    
# mylist = ["khushi","disha","tanvi","pooja","ankita",43,"mansi",45.0,"hemangi"]
# print(mylist)
# print(type(mylist))
# print(mylist[0])
# print(mylist[1])
# print(mylist[2])
# print(mylist[-1])
# print(mylist[2:5])
# print(mylist[:5])
# print(mylist[1:])
# print(mylist[1:8:2])
# print(mylist[:])
# print(mylist[::-1])

# mylist[6] = "Manthan"
# print(mylist)

# if "mansi" in mylist:
#     print("yes mansi is available")
# else:
#     print('not+ available')

# mylist.append('swaraj')
# mylist.append("rutuja")
# print(mylist)

# mylist.insert(1,"sanket")
# print(mylist)

# mylist.remove("hemangi")
# print(mylist)

# newlist = mylist.copy()
# print(newlist)

# mylist = [['khushi',['pawar']],[155,68],[416510,"xyz"]]
# print("example of multidimensional list:")
# print(mylist)
# # print(mylist[row][col])
# print(mylist[0][0])
# print(mylist[0][1])
# print(mylist[1][1])
# print(mylist[2][0])
# print(mylist[2][1])

# list1 = ['khushi','pawar']
# print(list1*2)

# list2 = [50,25,50]
# print(list1+list2)

# list2 = [50,25.50,'khushi']
# del list2[2]
# print(list2)
# list2.clear
# print(list2)

# name = "khushi"
# print(name)
# myname=list(name)
# print(myname)

# mylist = [40,30,20,10]
# mylist.reverse()
# print(mylist)

#  mylist = [44,22,77,0,9,88]
# mylist.sort()
# print(mylist)
# default sorting order for number is ascending order
# default sorting order for string is alphabetical order
# we should know that list should contaib homogeous

# Alising
# mylist = [44,22,77,0,9,88]
# newlist = mylist
# print(id(mylist))
# print(id(mylist))
# mylist[0] = "khushi"
# print(mylist)
# print(newlist)

# arr = [[1,2,3,4],
#        [4,5,6,7],
#        [8,9,10,11],
#        [12,13,14,15]]
# for i in range(0,4):
#     print(arr[i].pop())

# arr = [1,2,3,4,5,6]
# for i in range(1,6):
#     arr[i-1] = arr[i]
# for i in range(0,6):
#     print(arr[i],end=" ")

# a = [1,2,3,4,5,6,7,8,9]
# a[::2] = 10,20,30,40,50,60
# print (a)

# a = [1,2,3,4,5]
# print(a[3:0:-1])

# mytuple = ("khushi","disha","pooja","tanvi","mahi",23,3.15,77,"swaraj")
# # print (mytuple)
# print(type(mytuple))
# mytuple[2] = "sunil"
# # print(mytuple)

# init_tuple = ()
# print(init_tuple.__len__()) #0
# print(type(init_tuple.__len__()))

# init_tuple_a = 'a','b'
# init_tuple_b = ('a','b')
# print(id(init_tuple_a == init_tuple_b))

# init_tuple_a = '1','2'
# init_tuple_b = ('3','4')
# print(init_tuple_a + init_tuple_b)

# init_tuple = ('Python',) * 3
# print(type(init_tuple))#tuple

# init_tuple = (1,)*3
# init_tuple[0] = 2
# print(init_tuple) #init_tuple[0] = 2
# TypeError: 'tuple' object does not support item assignment

# init_tuple = ((1,2),)*7
# print(len(init_tuple[3:8])) #4

# names = [4,2,5,6,8,2]
# for i in names:
#     print(i)

# A = [4,0,2,5,0,1]
# for i in A:
#     if i ==0:
#         A.remove(i)
#         A.append(i)
# print(A)

# A = [1,2,2,3,4,4,5]
# newlist = []
# for i in A:
#     if i not in newlist:
#         newlist.append(i)
# print(newlist)
        
# A = [1,2,3]
# B = [2,3,4]
# C = [3,4,5]
# for i in A:
#     if i in B and i in C:
#         print(i) #3

# n = int(input("enter size of array: "))
# arr = []
# for i in range(n):
#     val = int(input("enter the value of array: "))
#     arr.append(val)
# sum=0 #12
# print(arr)#[10,11,7,12,14]
# for i in range(n):
#     if i+1 in range(n):
#         sum += abs(arr[i]-arr[i+1])#10-11 =1   
# print(sum)

# for i in range(1,5):
#     if i ==3:
#         break
#     print(i) #1,2
# for i in range(1,5):
#     if i ==3:
#         continue
#     print(i) #1,2,4

# #zip() inside we can take multiple range function
# for i,j in zip(range(1,6),range(5,0,-1)):
#     if i == 3 and j == 3:
#         continue
#     print(i,"  ", j)

# A = "Prashant*is*a*good*programmer"
# newname = ''
# val = ''
# for i in A:
#     if i != '*':
#         newname += i
#     else:
#         val+=i
# print(newname)
# print(str(val+newname))
        
# a = 50
# b = 30
# c = 20
# d = 10
# print((a+b)*c/d)
# print((a-b)*(c/d))
# print(a+(b*c)/d)

# x = ['A','B','C']
# y = ['A','B','C']
# z = [1,2,3,4]
# print(id(x==y))
# print(id(x==z))
# print(id(x!=z))

# str = "silent"
# str1 ='listen'

# if sorted(str) == sorted(str1):
#     print("anagram")
# else:
#     print("not anagram")
        
# str = "This is a my sentance"
# count =1
# for i in str:
#     if i == ' ':
#         count+=1
# print(count)

# Product of array
# given an array,return an array where each element is the product of all the elements in the array except itself.
# A = [1,2,3,4]


    
   




        
        