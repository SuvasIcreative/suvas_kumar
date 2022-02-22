"""26). Use a list comprehension to square each odd number in a list.
 The list is input by a sequence of comma-separated numbers.
Suppose the following input is supplied to the program:
1,2,3,4,5,6,7,8,9
Then, the output should be:
1,3,5,7,9"""



numbers = input("Type in: ")
#numbers = numbers.split(',')

odd_list = [i for i in numbers.split(',') if (int(i) % 2 != 0)]
print((" ").join(odd_list))