"""4). Write a program which accepts a sequence of comma-separated numbers from 
the console and generate a list and a tuple which contains every number. 
Suppose the following input is supplied to the program:
34,67,55,33,12,98
Then, the output should be:
['34', '67', '55', '33', '12', '98']
('34', '67', '55', '33', '12', '98')"""


number1 = list(map(int, input("\nEnter the numbers : ").split()))

print("\nList is - ", number1)

print("\nTuple is -", tuple(number1))
