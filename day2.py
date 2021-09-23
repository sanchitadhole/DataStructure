# import pandas as pd
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
# listA =[True, True]
# a = pd.Series(listA)
# print(a)
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
#
# listA = ['Monday','Tuesday','Wed','THu']
# listB = ['APPLE','MANGO','BANANA','CHIKU']
# print(pd.Series(index=listB,data = listA))
#
#
#
# d = {
#         "name":"chinmay",
#         "age":29,
#         "aged":29,
#         "ff":23
# }
#
# print(pd.Series(d))



import pandas as pd
a = {
    "name" : "chinmay",
    "age" : 20,
    "kb" : 6
}
print(pd.Series(a))