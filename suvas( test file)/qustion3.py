#
# # 3. Write a program to create a list of numbers, extract integer numbers from a list based on
# # below conditions.
# # a. Number must be 4 digit long i.e (1000 to 9999)
# # b. First digit of the number must be odd and the last digit must be even.
# # c. Number must be divisible by either 3 or 7.
#
#
# list1 = [4254, 5564, 4861, 8875, 6935, 556, 5456665,'str',True,'5545']
#
# new_list=filter(lambda x: x in range(1000,9999)  and int(str(x)[0]) % 2 == 0
#  and x % 2 == 0 and (x % 3 == 0 or x % 7 == 0), list1)
#
# print(list(new_list))


# l1=[1000,2000,3000,7000,5000,10000,900,30,'gfgt']
#
# print(list(filter(lambda x:x in range(1000,9999) and int(str(x)[0])%2 !=0 and int(str(x)[-1])%2 ==0 and (x%3==0 or x%7==0) ,l1)))
#
# """--RE-P2--- Write a program to extract string elements from a list based on below conditions, use
# in-built functions.
# a. First character must capitalize and consonant.
# b. String must not contain any number."""
#
#
# l1=["Xyz","abc","Bcd ji","Ssd",555,5]
# l2=['a','e','i','o','u','A','E','I','O','U']
#
#
# print(list(filter(lambda x:type(x)==str and x[0] not in l2 and x == x.capitalize(),l1)))

# matrix = [5,[1, 2, 3], [4, 5], [6, 7, 8, 9]]
#
# # Nested List Comprehension to flatten a given 2-D matrix
# flatten_matrix = [val for sublist in matrix for val in sublist if val%2==0]
#
# print(flatten_matrix)
# from collections import Iterable
# def flatten(lis):
#     for item in lis:
#         if isinstance(item, Iterable) and not isinstance(item, str):
#             for x in flatten(item):
#                 yield x
#         else:
#             yield item
# lis = [1,[2,2,2],4]
# list(flatten(lis))
#
# L = [[1, 2, 3],[4, 5, 6],[7, 8, 9,8,9]]
# for list in L:
#     for number in list:
#         print(number, end=' ')
# # Prints 1 2 3 4 5 6 7 8 9


# Python program to flatten a nested list

# explicit function to flatten a
# nested list
# def flattenList(nestedList1):
#     # check if list is empty
#     if not (bool(nestedList1)):
#         return nestedList1
#
#     # to check instance of list is empty or not
#     if isinstance(nestedList1[0], list):
#
#         # call function with sublist as argument
#         return flattenList(*nestedList1[:1]) + flattenList(nestedList1[1:])
#
#     # call function with sublist as argument
#     return nestedList1[:1] + flattenList(nestedList1[1:])
#
#
# # Driver Code
# nestedList = [12,45,13,14.5,12.6,'65','78',[75,4,62,'42','def',[84,96,'42.2']]]
# print('Nested List:\n', nestedList)
# x=flattenList(nestedList)
# print("Flattened List:\n", flattenList(nestedList))
# print(x)
# for i in x:
#     if type(i)==int:
#         if i%2==0:
#             print(i)

#
# list1=[5,5.5,'str',[1], [2], [3], [4], [5,8,[9]],4,(4,3)]
# def func(das):
#     if not (bool(das)):
#         return das
#     if isinstance(das[0],list):
#         return func(*das[:1])+func(das[1:])
#     return (das[:1])+func(das[1:])
# x=func(list1)
# print(x)
# new_list=list(filter(lambda i:type(i)==int and i%2==0,x))
# print(new_list)

# x=[(2,5),(5,8)]
# # y=(map(lambda i:sum(i),x))
# # print(list(y))
# def fun(x):
#     return map(lambda i:sum(i),x)
# print(list(fun(x)))