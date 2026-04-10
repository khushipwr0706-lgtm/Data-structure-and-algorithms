# import re
# count = 0
# pattern = re.compile('function')
# # print(matcher)
# matcher = pattern.finditer('A function is a fundamental concept in mathematics that describes a specific relationship between two sets, where each element in the first set (known as the domain or input) is assigned to a unique element in a second set (known as the range or output). ')
# for i in matcher:
#     count += 1
#     print(i.start(),'...',i.end(),'...',i.group())
# print('The number of occurence: ',count)

# import re
# count = 0
# matcher = re.finditer('Hi','HiHiHiHi')
# for i in matcher:
#     count += 1
#     print(i.start(),"...",i.end(),'...',i.group())
# print('The number of occurrences:',count)

# import re
# obj = input('enter any character')
# objmatch= re.finditer(obj,'a7b @k9z')
# for match in objmatch:
#     print(match.start(),'...',match.end(),'...',match.group())
 
# match() :- it can be used only for beginning level    
# import re
# a = input('enter string to perform match operation :')
# mh = re.match(a,"python is very important language")
# print(mh)
# if mh != None:
#     print('match not found at beginning  level')
#     print(mh.start()," ", mh.end())
# else:
#     print('there is no matching at beginning level')
    
# fullmatch():-As a name suggest when we have to match full string with the given pattern them we have to use fullmatch()function
# it can be used for full string found 
# import re
# a = input('enter string to perform match operation :')
# mh = re.fullmatch(a,"pythonisvery")
# print(mh)
# if mh != None:
#     print('match found ')
#     print(mh.start()," ", mh.end())
# else:
#     print('there is no matching at beginning level')

# Search()
# if the match found anywhere in the string then it return object else it will return None
# import re
# a = input('enter string to perform match operation :')
# mh = re.search(a,"python sss dynamic lann")
# print(mh)
# if mh != None:
#     print('match found ')
#     print(mh.start()," ", mh.end(),' ',mh.group())
# else:
#     print('there is no matching anywhere')

# to read a file using search()method
# 


# findall()
# this function return a list which containing all matches
# import re
# mh = re.findall('[0-9]' , 'abcdDeHKHUSHIlam209817fkadisha')
# print(mh)
# import re
# mh = re.findall('[a-z]' , 'abcdDeHKHUSHIlam209817fkadisha')
# print(mh)
# import re
# mh = re.findall('[A-Z]' , 'abcdDeHKHUSHIlam209817fkadisha')
# print(mh)
# import re
# mh = re.findall('[0-9a-zA-z]' , 'abcdDeHKHUSHIlam209817fkadisha')
# print(mh)
# import re
# mh = re.findall('[^0-9a-zA-z]' , 'abcdDeHKHUSHIlam209817fkadisha')
# print(mh)

# sub()
# This function perform substitution or replacement re.sub(expression,replacement,string)here every match pattern will be replaced by provided replacement
# import re
# obj = re.sub('[a-zA-Z]','X','2345 ABCD fabc deff')
# print(obj)
# import re
# obj = re.sub('[a-zA-Z]','*','2345 ABCD fabc deff')
# print(obj)

# subn()
# It is as similar as sub()function only one thing is different i.e also return no. of replacements. this return in tuple where first element is string and second one is no. of replacement 
# import re
# obj = re.subn('[0-7]','@','ab3gd6nkl7')
# print(obj)
# print('the string is=',obj[0])
# print('the number of replacement is=',obj[1])

# import re
# mo = input('enter mobile number')
# obj = re.fullmatch("[0-9]\d{9}",mo)
# if obj!=None:
#     print('valid mobile number')
# else:
#     print('invalid mobile number')

# import re 
# s = input('enter mail id:')
# m = re.fullmatch('\w[a-zA-Z0-9_.]*@ybit.ac.in', s)
# if m!=None:
#     print('Valid E-mail Id')
# else:
#     print('Invalid E-mail Id')

# import os,sys
# fname = input('enter file name')
# if os.path.isfile(fname):
#     print('file exits:',fname)
#     f=open(fname,'r')
# else:
#     print('file does not exists:',fname)
#     sys.exit(0)
# print('the content of file is:')
# data=f.read()
# print(data)
# split()
# This function is used to split the given string as per the some pattern then we 

 