# Recursion
# def powerOfTwo(n):
#     if n == 0:
#         return 1
#     else:
#         power = powerOfTwo(n-1)
#         return power * 2

# loop
# def poweOfTwoIt(n):
#     i = 0
#     power = 1
#     while i < n:
#         power = power * 2
#         i = i + 1
#     return power


# def Factorial(num):
#     if num <= 1:
#         return 1
#     return num * Factorial(num-1)
# print(Factorial(4))#24

# def isPalindrome(strng):
#     if len(strng) == 0:
#         return True
#     if strng[0] != strng[len(strng)-1]:
#         return False
#     return isPalindrome(strng[1:-1])

# print(isPalindrome('awesome'))
# print(isPalindrome('foobar'))
# print(isPalindrome('tacocat'))

# def power(base, exponenet):
#     if exponenet == 0:
#         return 1
#     return base * power(base, exponenet-1)
# print(power(2,0))
# print(power(2,2))
# print(power(2,4))

# def capitalizeFirst(arr):
#     result = []
#     if len(arr) == 0:
#         return result
#     result.append(arr[0][0].upper() +arr[0][1:])
#     return result + capitalizeFirst(arr[1:])
# print(capitalizeFirst(['car','taco','banana']))

# def productOfArray(arr):
#     if len(arr) == 0:
#         return 1
#     return arr[0] *productOfArray(arr[1:])
# print(productOfArray([1,2,3]))
# print(productOfArray([1,2,3,10]))

# def fib(num):
#     if (num < 2):
#         return num
#     return fib(num -1) + fib(num - 2)
# print(fib(4))
# print(fib(10))
# print(fib(28))
# print(fib(35))

# class Tree:
#     def __init__(self,data):
#         self.data = data#instance variable(create separate memory for each obj)
#         self.children = []
#     def addChild(self,child):
#         self.children.append(child)
#     def __str__(self,level = 0):
#         ret = ' '* level +str(self.data) +'\n'
#         for child in self.children:
#             ret += child.__str__(level+1)
#         return ret
    
# rootNode = Tree('Drinks')
# hot      = Tree('Hot')
# cold     = Tree('Cold')
# tea      = Tree('tea')
# coffee    =Tree('coffee')
# nonAlchohlic = Tree('Nonalchohlic')
# alchohlic    =Tree('Alchohlic')

# # add child noddes in tree
# rootNode.addChild(hot)
# rootNode.addChild(cold)
# hot.addChild(tea)
# hot.addChild(coffee)
# cold.addChild(nonAlchohlic)
# cold.addChild(alchohlic)

# print(rootNode)

# class Tree:
#     def __init__(self,data):
#         self.data = data 
#         self.children =[]

#     def addChild(self, child):
#         self.children.append(child)

#     def __str__(self, level =0):
#         ret =" "* level + str(self.data) + "\n"
#         for child in self.children:
#             ret += child.__str__(level+1)
#         return ret
    
    
# rootNode = Tree("N1")
# n2 = Tree("N2")
# n3 =Tree("N3")
# n4 = Tree("N4")
# n5 = Tree("N5")
# n6 = Tree("N6")
# n7 = Tree("N7")
# n9 = Tree("N9")
# n10 = Tree("N10")

# rootNode.addChild(n2)
# rootNode.addChild(n3)
# n2.addChild(n4)
# n2.addChild(n5)
# n3.addChild(n6)
# n3.addChild(n7)
# n4.addChild(n9)
# n4.addChild(n10)

# print(rootNode)

# class BSTNode:
#     def __init__(self , data):
#         self.data = data
#         self.leftChild = None
#         self.rightChild = None
#     def insertNode(rootNode,nodeValue):
#         if rootNode.data == None:
#             rootNode.data = nodeValue
#         elif nodeValue <= rootNode.data:
#             if rootNode.leftChild is None:
#                 rootNode.leftChild = BSTNode(nodeValue)
#             else:
#                 insertNode(rootNode.leftChild,nodeValue)
#         else:

class Node:#create a separate node
    def __init__(self , value):
        self.value = value
        self.left = None
        self.right = None
class BinaryTree:
    def __init__(self):
        self.root = None
    def insert(self,value):
        #insert root node  in if block if there is no root node
        if self.root is None:
            self.root = Node(value)
        else:
            self.insertNode(self.root,value)
    def insertNode(self,rootNode,value):
        if value < rootNode.value:
            if rootNode.left is None:
                rootNode.left = Node(value)
            else:
                self.insertNode(rootNode.left,value)
        else:
            if rootNode.right is None:
                rootNode.right = Node(value)
            else:
                self.insertNode(rootNode.left,value)
        
btObj = BinaryTree()
btObj.insert(50)
btObj.insert(30)
btObj.insert(70)
print(btObj)    


        

        