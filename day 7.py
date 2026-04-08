# A = {'C':3,'B':2,'A':1}
# B = {}
# for i in sorted(A):
#     B = sorted(A).items()
#     print(B)
#     print(A)

# import sys
# class Queue:
#     def __init__(self, queueSize):#parameterize constructor
#         self.queueList = []#stack created
#         self.queueSize = queueSize
        
#     def isFull(self):
#         if len(self.queueList) == self.queueSize:
#             return True
#         else:
#             return False
        
#     def Enqueue(self,value): #add element in queue from rear
#         if self.isFull():
#             print('Queue is full')
#         else:
#             self.queueList.append(value)
#     def displayQueue(self):
#         print('=========================')
#         print(self.queueList)
#         print('=========================')
#     def isEmpty(self):
#         if self.queueList == []:
#             return True
#         else:
#             return False
#     def Dequeue(self):
#         if self.isEmpty():
#             return "Queue is Empty"  
#         else:
#             self.queueList.pop(0)
#     def deleteQueue(self):#delete the queue
#         self.queueList = None 
#         return "Queue is Delete"
#     def peek(self):  # it returns 1st element of queue
#       if self.queueList is None:
#         return "Queue is deleted"
#       elif self.isEmpty():
#         return "Queue is empty"
#       else:
#         return self.queueList[0]

# size = int(input('Enter the size of Queue'))
# queueObj = Queue(size)#queue object has created
        
# while True:
#     print("1.Enqueue Element in Queue:")
#     print("2.Display Queue elements:")
#     print("3.check Queue is Empty")
#     print("4.Dequeue operation in Queue :")
#     print('5.Delete Queue')
#     print('6.Show Top Element from queue')
#     print('7.Exit')
#     choice = int(input('Enter your choice :'))
#     if choice == 1:
#         val = int(input('Enter the value for Queue:'))
#         queueObj.Enqueue(val)
#     elif choice ==2:
#         queueObj.displayQueue()
#     elif choice == 3:
#         print(queueObj .isEmpty())
#     elif choice==4:
#         print(queueObj.Dequeue())
#     elif choice == 5:
#         print(queueObj.deleteQueue())
#     elif choice == 6:
#         print(queueObj.peek())
#     elif choice == 7: 
#         sys.exit()
        
# def findBiggestNumber(array):#[2,4,5,6,7,1,9,3,4,5,6]
#     firstValue = array[0] #firstValue = 4 ====>O(1)---any assignment statements and if statements that are executes once regardless of the size of the problem
#     for i in range(1,len(array)):#i=1 ===>O(N) --- a simple 'for'loop from 0 to n(with no internal loops)
#         if array[i] >firstValue:#4 > 2 ===>O(1)
#             firstValue = array[i] #4 ===>O(1)
#     return firstValue #====>O(1)

# array = [2,4,5,6,7,1,9,3,4,5,6]
# print(findBiggestNumber(array))
        # O(n^2)---A nested loop of the same type takes qadratic time complexity
        # O(log n) ---- A loop in which the controling parameter is divided by two at each step
        
# A = 'gasgg54@#vscsdls'
# count = 0
# for i in A:
#     z = ord(i)
#     print(z)
#     if z>=97 and z<=122:
#         continue
#     elif z>=48 and z<=57:
#         continue
#     else:
#         count += 1
# print(count)

# class List:
    
#     def __init__(self,areaSize):
#         self.areaSize = areaSize
#     def insert(self,A):
#         self.A = A
#     def square(self,square,B):
#         self.square = square
#         for i in B:
#             if square/2 == 0:
#                 print("it is square")
#             else:
#                 print("it is not square")
            
     
        
        
         
# size = int(input('Enter the size of List'))
# list1obj = List(size)
# while True:
#     print("1 . Enter the size of number")
#     print("2 . Enter the number")
#     choice = int(input('Enter your choice :'))
#     if choice == 1:
#        val = int(input('Enter the value for List:'))
#        list1obj.areaSize()
#     if choice == 2:
#        val = int(input('Enter the number'))
#        list1obj.insert()
#     if choice == 
       
# Linear search
# def linearSearch(array,target):
#     for i in range(len(array)):
#         if array[i] == target:
#             return i 
#     return -1
# array = [1,2,3,4,5,6,7,8,9]
# target = 4
# result = linearSearch(array,target)
# if result == -1:
#     print("Not found")
# else:
#     print("Element found at index no =",result)

# Binary Search
# def binarySearch(array,target):
#     start = 0
#     end = len(array)-1
#     while start <= end:
#         mid = (start+end)// 2
#         if array[mid] == target:
#             return mid 
#         elif array[mid] < target:
#             start = mid+1
#         else:
#             end = mid -1
#     return -1
# sortedArray = [1,2,3,4,5,6,7,8,9]
# target = 55
# result = binarySearch(sortedArray,target)
# if result == -1:
#     print("Not found")
# else:
#     print("Element found at index no =",result)
       
# class Node:
#     def __init__(self,data):
#         self.data = data#insatance variable
#         self.next = None
# class LinkedList:
#     def __init__(self):
#         self.head = None

# linkedlist = LinkedList()
# linkedlist.head = Node(5)#1st node
# second          = Node(10)
# third           = Node(15)
# fourth          = Node(20)

# #linking part
# linkedlist.head.next = second
# second.next = third
# third .next = fourth

# print(linkedlist.head.data)
# print(second.data)
# print(third.data)
# print(fourth.data)

# print(linkedlist.head.next)
# print(second.next)
# print(third.next)
# print(fourth.next)


# # display Linkedlist
# while linkedlist.head != None:
#     print('|',linkedlist.head.data,"|",linkedlist.head.next,"->",end =" ")
#     linkedlist.head = linkedlist.head.next
