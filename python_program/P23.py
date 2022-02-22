
#By using list comprehension, please write a program 
#to print the list after removing the value 24 in [12,24,35,24,88,120,155]


list1 = [12, 24, 35, 24, 88, 120, 155]

new_list = [x for x in list1 if x != 24]
print(new_list)