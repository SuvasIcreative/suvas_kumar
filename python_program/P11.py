"""11). Use a list comprehension to square each odd number in a list.
 The list is input by a sequence of comma-separated numbers.
Suppose the following input is supplied to the program:
1,2,3,4,5,6,7,8,9
Then, the output should be:
1,3,5,7,9
"""

t= (5, 11,4,7, 3,2,6,8,9)
tup=[x**2 for x in t if x%2!=0]

print(tup)