# Arributes of array

from numpy import *

arr1 = array([1,2,3,4,5])
print(arr1.ndim)

arr2 = array([

    [1,3,4],
    [4,5,6]

])
print(arr2.ndim)


arr3 = array([

[

    [1,3,4],
    [4,5,6]

],

[

    [1,3,4],
    [4,5,6]

]


])

print(arr3.ndim)
arr4 = array([2,3,4,5,6,6])
print(arr4.shape)

print(type(6))


arr5 = array([
    [2,3,4,5,6,6],
    [3,4,5,7,87,8]

]

)
print(arr5.shape)

arr4 = array([3 ,4,5,6,7,8])
print(arr4.size)


print(array([

    [3 ,4,5,6,7,8],
    [3, 4, 5, 6, 7, 4]

]).size)


arr55 = array([3,4,4,5,6])
print(arr55.dtype)


arr66 = array([3.7,4.7,4.8,5.8,6.9])
print(arr66.dtype)


# 121 -  121
#121
a = 121
b = str(a)
c = b[::-1]
if b == c:
    print('Number is pallindrome')

# --



# The reshape


# arrc = arange(10)
# print(arrc)
#
# print(arrc.reshape(2,5))
# print(arrc.reshape(5,2))
#
# arrd = arange(35)
# print(arrd.reshape(5,7))
# print(arrd.reshape(7,5))
#
# print(type(arrd))


# arr3 = [
#
#         [1,2,3,4,5,6],
#         [3,4,5,6,7,6]
#
# ]
# print(arr3.shape)
# arr3.shape = (3,4)
# print(arr3.shape )
#

#
# a = {
#
#     'a':12,
#     'b':24
#
# }
#
# print(a['a'])
#
# a['a'] = 23
#
# print(a)

# Flatten



arrc = array([ [1,2,3,4,5],
                [2,3,4,5,3],
                [2,3,44,55,35]
               ]
             )
print(arrc.ndim)

print(arrc.flatten())

# The ones and zeros


# c = ones((rows,col),dtype)
c = ones((2,3))
cd = zeros((2,3))

print(c)
print(cd)

w = array([
                [

                [1,2,3],
                [2,4,5]
                ],

                [

                    [1,266,3],
                    [2,4,5]


                ]

        ])


print(w[1][0][1])