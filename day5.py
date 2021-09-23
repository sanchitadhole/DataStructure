import pandas as pd


#
#
# # Creating a series from python
#
#
# # Weather report -- > 5  --- > AC , Medical boost
# # chnadrapur 100
# # Pune  --
# # Mumbai ---
# # Delhi
# # Bajaj allianze -- Nihilent
#
# listA =['A','B','C','D']
# a = pd.Series(listA)
# print(a)
#
#
listA =[True, True]
a = pd.Series(listA)
print(a)
#
#
# listA =[1,2]
# a = pd.Series(listA)
# print(a)
#
#
# listA =[1.2,3.4]
# a = pd.Series(listA)
# print(a)
#
#
# # Properties
# print(a.values)
# print(a.ndim)
# print(a.dtype)
#
#
#
# # Methods
# print(a.sum())
# print(a.product())
# print(a.max())
# print(a.min())
#
#
#
# # Excel ---
#
#
#
#
#
#
#
#
#
# # attribute method??   --- belong tp class  -- object
# # artribute -
# # color  - white
# # parameter - argument
# # method
#
# #-------------------------------------------
# # listA = ['Monday','Tuesday','Wed','THu']
# # listB = ['APPLE','MANGO','BANANA','CHIKU']
# # print(pd.Series(index=listB,data = listA))
# #
# # #---------------------------------------------
# # d = {
# #         "name":"chinmay",
# #         "age":29,
# #         "aged":29,
# #         "ff":23
# # }
# #
# # print(pd.Series(d))
# #
# #
# #
# #
# #
# #
# #
# #
# # x = int(input('Please enter the number of string')) #5
# #
# # k = []
# # for y in range(x):
# #     c = input('Please enter string') # Mango
# #     k.append(c)
# #
# #
# # print(k)
# #
# # userInput = input('Which fruit positoon you want to knpow')
# #
# # print(k.index(userInput))
# #
# #
# #
# #
# #
# #
# #
# # # shirt ----  S ,M, L,XL
# #
# #
# # # duplicate
# #
# # # sort
# #
# # # asc
# #
# # # des
# # # 3 colum
# #
# # # 4 sum
#
# # relevanmt - same data type
#
# # array and list -- major difference
#
#
# #array - same data type
# #list - different
#
#
# lista= [1,2,3,4,5]
#
# a = pd.Series(lista)
# # Series is nothing but single dimesnional arry
# print(a)
#
#
# listb = ['chinmay','sarika','amol','chinmay2']
# b = pd.Series(listb)
# print(b)
#
#
# listc = [23,45.0,55,66,77.9,66,77]
# c = pd.Series(listc)
# print(c)
#
#
#
# # attributes
#
# #-------- series ---------  values , dtype , index
#
# print(c.values)
# print(type(c.values))
# print(c.dtype)
# print(c.index)
#
#
#
# print(c.sum())
# print(c.mean())
# print(c.product())
#
#
#
# person = {
#
#     'name':'chinmay',
#     'lastname':'deshpande',
#     'age':30,
#
#
# }
# print('******')
# ser = pd.Series(person)
# print(ser)
#
#
#
# a = ['A','B','C','D']
# b = [1,2,3,4]
# z = pd.Series(b,a,object,'chinmay')
# print(z)
#
# s = pd.Series(index = b ,data =a ,dtype= object ,name ='chinmay')
# print(s)
#
#
#
#
# a = pd.read_csv("day.csv",error_bad_lines=False)
# print(a)


# def add(y,x):
#     print(x/y)
#
# add(x =10 ,y= 20)

# 10/5
#
# 5/10


# listA = [2,3,4,5,5]
# sum = 0
# for item  in listA:
#     sum += item
# print(sum)
#
#


#
#
# # class person:
# #
# #     age = 10
# #
# #     def ac(self):
# #         print('hello')
# #
# #
# # a = person()
# # a.age
# # a.ac()
#
#
#
#
#
#
#
# #link list
#
# # linked list
#
# # stack
#
# # queue
#
# # D queue
#
#
# ll = []
#
# ll.append("A")
# ll.append("B")
# ll.append("C")
#
# print(f"The link list is {ll}")
#
# choice = 0
#
# while choice < 5:
#     print('Linked list operations')
#     print('1 to add the elements')
#     print('2 to remove the elements')
#     print('3 to replace the elements')
#     print('4 Search for the element')
#     print('5 Exist the program')
#
#     choice = int(input('Your choice'))
#
#     if choice == 1:
#         ele = input('Enter the element')
#         pos = int(input('Enter the position'))
#         ll.insert(pos, ele)
#
#
#     elif choice == 2:
#
#         try:
#             ele = input('Enter the element to removed')
#             ll.remove(ele)  # error
#         except ValueError:
#             print('Element not in the list')
#
#
#
#     elif choice == 3:
#         ele = input('Enter the element')
#         pos = int(input('Enter the position'))
#         ll.pop(pos)
#         ll.insert(pos, ele)
#
#
#     elif choice == 4:
#         try:
#             ele = input('please Enter the element to be searched')
#             pos = ll.index(ele)
#             print(pos)
#         except ValueError:
#             print('Element not in the list')
#
#     else:
#         break
#
# print(f'The upated list is {ll}')
#
#
# # Stack
#
# # Pop
# #
# # pusp
# #
# # peep
#
# # empty
#
#
# # LIFO
#
#
# class Stack:
#     isEmpty = False
#
#     def init(self):
#         self.st = []
#
#     def isempty(self):
#         return self.st == []
#
#     def pop(self):
#         if self.isempty():
#             self.isEmpty = True
#         else:
#             return self.st.pop()
#
#     def push(self, element):
#         if self.isempty():
#             self.isEmpty = True
#         else:
#             self.st.append(element)
#
#     def peep(self):
#         if self.isempty():
#             self.isEmpty = True
#         else:
#             return self.st[len(self.st) - 1]
#
#     def display(self):
#         if self.isEmpty:
#             print('List is blank')
#         else:
#             print(self.st)
#
#
# stt = Stack()
# choice = 0
#
# while choice < 5:
#
#     print('Linked list operations')
#     print('1 to remove the elements')
#     print('2 to push the elements')
#     print('3 to view upper element without deleting')
#     print('4 display')
#     choice = int(input('Your choice'))
#
#     if choice == 1:
#         print(stt.pop())
#
#     elif choice == 2:
#         ele = input('Please Enter the element')
#         stt.push(ele)
#         stt.display()
#     elif choice == 3:
#         print(stt.peep())
#
#     elif choice == 4:
#         stt.display()
#
#     else:
#         break
#
#


#  Queue
#
class Queue:
    def _init_(self):
        self.qu = []

    def isempty(self):
        return self.qu == []

    def add(self, element):
        self.qu.append(element)

    def delete(self):
        if self.isempty():
            return -1
        else:
            return self.qu.pop(0)

    def search(self, element):
        if self.isempty():
            return -1
        else:
            try:
                n = self.qu.index(element)
                return n + 1
            except ValueError:
                return -2

    def display(self):
        print(self.qu)


# a = reversed([12,33,44,55,666])
#
# for item in a:
#     print(a)

q = Queue()

choice = 0

while choice < 5:

    print('Queue list operations')
    print('1 to delete the elements')
    print('2 to add the elements')
    print('3 to search upper element without deleting')
    print('4 display')
    print('5 to exist')
    choice = int(input('Your choice'))

    if choice == 1:
        a = q.delete()
        if a == -1:
            print('Queue is empty')
        else:
            print('The delete element is {}'.format(a))

    elif choice == 2:
        q.add(input('Enter the string : '))
        print('Element added successfullt')

    elif choice == 3:
        qa = q.search(input('Enter the string : '))

        if qa == -1:
            print("queue list is empty")
        elif qa == -2:
            print('Element not found')
        else:
            print(f'Element found at postion {qa}')

    elif choice == 4:
        q.display()

    else:
        break

from _collections import deque

d = deque()

print('Queue list operations')
print('1 add element from first')
print('2 add element to the last ')
print('3 del element from the first')
print('4 del elemement from the last')
print('5 del the element in between')
print('6 search the element')
print('7 exist the element')
choice = int(input('Your choice'))

if choice == 1:
    d.appendleft(input('Enter the element'))
elif choice == 2:
    d.append(input('Enter the element'))
elif choice == 3:
    d.popleft()
elif choice == 4:
    d.pop()
elif choice == 5:
    try:
        d.remove(input('Enter the element to be removed'))
    except:
        print("Element not present")
elif choice == 5:
    a = d.index("Enter the element to be searched")
    print(a + 1)

else:
    break