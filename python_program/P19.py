"""19). Please write a program to print the list 
after removing delete even numbers in [5,6,77,45,22,12,24]."""

list1=[5,6,77,45,22,12,24]
x=[i for i in list1 if i%2!=0]
print(x)
#
# removing_even_number=[]
#
# for i in list1:
# 	if i%2!=0:
# 		removing_even_number.append(i)
#
# print(removing_even_number)
#
