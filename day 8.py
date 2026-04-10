# import sys
# class Node:
#     def __init__(self,data):
#         self.data = data
#         self.next = None
# class LinkedList:
#     def __init__(self):
#         self.head = None
#         self.tail = None
#     def addNode(self,value):
#         node = Node(value)
#         if self.head is None:
#             self.head = node
#             self.tail = node
#         else:
#             self.tail.next = node
#             self.tail      = node
#     def displayNode(self):
#         print('----------------------------------')
#         while self.head is not None:
#           print('|',self.head.data,'|',self.head.next,'->',end=' ')
#           self.head = self.head.next
#         print('----------------------------------')
#     def addNodeBeginning(self,value):
#         node = Node(value)
#         if self.head is Node:
#             self.head = node
#             self.tail = node
#         else:
#             node.next = self.head
#             self.head = node
#     def addNodeBetween(self,index,value):
#         node = Node(value)
#         if self.head is None:
#             self.head = node
#             self.tail = node
#         elif index == 0:
#             node.next = self.head
#             self.head = node
#         else:
#             temp = self.head
#             for _ in range(index-1):
#                 temp = temp.next
#             node.next = temp.next
#             temp.next = node
#     def addNodeEnd(self,value):
           
# if __name__ == '__main__':
#     object = LinkedList()

# while True:
#     print("1. Add Node Linkedlist :")
#     print("2. Add Node  Begining :")
#     print("3. Add Node Between :")
#     print("4. Add Node End :")
#     print("5. Display Linked LIst :")
#     print("6. Exit :")
#     ch = int(input('Enter the choice'))
#     if ch == 1:
#         value = int(input('Enter value for node:'))
#         object.addNode(value)
#         print("Node added successfully")
#     elif ch == 2:
#         value = int(input("enter value for "))
#         object.addNodeBeginning(value)
#     elif ch == 3:
#         value = int(input('enter value and add node in between'))
#         index = int(input('Enter position after that you have to insert:'))
#         object.addNodeBetween(index,value)
#         print('Node added successfully in Between:')
#     elif ch == 4:
#         value = int(input('enter value for node in End'))
#         object.addNodeEnd(value)
#     elif ch == 5 :
#         object.displayNode()
#     elif ch == 6:
#         sys.exit()
        
        
# class Matrix:
#   def input_matrix(self,rows,cols):
#     matrix = []
#     for i in range(rows):
#         rows = []
#         for j in range(cols):
#             val = int(input())
#             rows.append(val)
#             matrix.append(rows)
#             return matrix
#   def display(self,matrix,rows,cols):
#       for i in range(rows):
#           for j in range(cols):
#               print(matrix[i][j], end=" ")
#               print()

# A = [0,0,1,2,0,3,0,0,4]
# print(A[2:])

A = [0,0,1,2,0,3,0,0,4]
for _ in range(2):
    if 0 in A:
        A.remove(0)
print(A)
    