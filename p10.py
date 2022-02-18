# # # # def factorial(x):
# # # #     """This is a recursive function
# # # #     to find the factorial of an integer"""
# # #
# # # #     if x == 1:
# # # #         return 1
# # # #     else:
# # # #         return (x * factorial(x-1))
# # #
# # #
# # # # num = 5
# # # # a=factorial(5)
# # # # print(a)
# # # # print("The factorial of", num, "is", factorial(num))
# # #
# # #
# # #
# # #
# # # def recursive_fibonacci(n):
# # #    if n <= 1:
# # #        return n
# # #    else:
# # #        return(recursive_fibonacci(n-1) + recursive_fibonacci(n-2))
# # #
# # # n_terms = 10
# # #
# # # # check if the number of terms is valid
# # # if n_terms <= 0:
# # #    print("Invalid input ! Please input a positive value")
# # # else:
# # #    print("Fibonacci series:")
# # #    for i in range(n_terms):
# # #        print(recursive_fibonacci(i))



# # def sum(n):
# #     if n > 0:
# #         return n + sum(n-1)
# #     return 0


# # result = sum(100)
# # print(result)







# # Python program to flatten a nested list

# # explicit function to flatten a
# # nested list
# def flattenList(nestedList):

#     # check if list is empty
#     if not(bool(nestedList)):
#         return nestedList

#     # to check instance of list is empty or not
#     if isinstance(nestedList[0], list):

#         # call function with sublist as argument
#         return flattenList(*nestedList[:1]) + flattenList(nestedList[1:])

#     # call function with sublist as argument
#     return nestedList[:1] + flattenList(nestedList[1:])


# # Driver Code
# nestedList = [[1,[5,[10,[5,10,5,[4]]]]], [2], [3], [4], [5]]
# print('Nested List:\n', nestedList)

# print("Flattened List:\n", flattenList(nestedList))







# def flatten(S):
#     if S == []:
#         return S
#     if isinstance(S[0], list):
#         return flatten(S[0]) + flatten(S[1:])
#     return S[:1] + flatten(S[1:])

# s=[[1,[5,[3,[2]]],2],[3,4]]
# print("Flattened list is: ",flatten(s))





def check_eq(mast_dict, subdict):
    if not isinstance(mast_dict, (dict, list)):
        return mast_dict == subdict
    if isinstance(mast_dict, list):
  
        # check for nesting dictionaries in list
        return all(check_eq(x, y) for x, y in zip(mast_dict, subdict))
  
    # check for all keys
    return all(mast_dict.get(idx) == subdict[idx] or check_eq(mast_dict.get(idx), subdict[idx]) for idx in subdict)
  
  
def is_subset(mast_dict, subdict):
    if isinstance(mast_dict, list):
  
        # any matching dictionary in list
        return any(is_subset(idx, subdict) for idx in mast_dict)
  
    # any matching nested dictionary
    return check_eq(mast_dict, subdict) or (isinstance(mast_dict, dict) and any(is_subset(y, subdict) for y in mast_dict.values()))
  
  
# initializing dictionary
test_dict = {"gfg": 12, 'best': {1: 3, 4: 3, 'geeks': {8: 7}}, 'cs': 7}
  
# printing original dictionary
print("The original dictionary is : " + str(test_dict))
  
# initializing subset dict
sub_dict = {8: 7}
  
# calling func
res = is_subset(test_dict, sub_dict)
  
# printing result
print("Is dictionary subset : " + str(res))