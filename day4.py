# linked list

# stack

# queue

# D queue


ll = []

ll.append("A")
ll.append("B")
ll.append("C")

print(f"The link list is {ll}")

choice = 0

while choice < 5:
    print('Linked list operations')
    print('1 to add the elements')
    print('2 to remove the elements')
    print('3 to replace the elements')
    print('4 Search for the element')
    print('5 Exist the program')

    choice = int(input('Your choice'))

    if choice == 1:
        ele = input('Enter the element')
        pos = int(input('Enter the position'))
        ll.insert(pos, ele)


    elif choice == 2:

        try:
            ele = input('Enter the element to removed')
            ll.remove(ele)  # error
        except ValueError:
            print('Element not in the list')



    elif choice == 3:
        ele = input('Enter the element')
        pos = int(input('Enter the position'))
        ll.pop(pos)
        ll.insert(pos, ele)


    elif choice == 4:
        try:
            ele = input('please Enter the element to be searched')
            pos = ll.index(ele)
            print(pos)
        except ValueError:
            print('Element not in the list')

    else:
        break

print(f'The upated list is {ll}')


# Stack

# Pop
#
# pusp
#
# peep

# empty


# LIFO


class Stack:
    isEmpty = False

    def _init_(self):
        self.st = []

    def isempty(self):
        return self.st == []

    def pop(self):
        if self.isempty():
            self.isEmpty = True
        else:
            return self.st.pop()

    def push(self, element):
        if self.isempty():
            self.isEmpty = True
        else:
            self.st.append(element)

    def peep(self):
        if self.isempty():
            self.isEmpty = True
        else:
            return self.st[len(self.st) - 1]

    def display(self):
        if self.isEmpty:
            print('List is blank')
        else:
            print(self.st)


stt = Stack()
choice = 0

while choice < 5:

    print('Linked list operations')
    print('1 to remove the elements')
    print('2 to push the elements')
    print('3 to view upper element without deleting')
    print('4 display')
    choice = int(input('Your choice'))

    if choice == 1:
        print(stt.pop())

    elif choice == 2:
        ele = input('Please Enter the element')
        stt.push(ele)
        stt.display()
    elif choice == 3:
        print(stt.peep())

    elif choice == 4:
        stt.display()

    else:
        break