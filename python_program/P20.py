"""20). By using list comprehension, please write a program 
to print the list after removing delete numbers which are 
divisible by 5 and 7 in [12,24,35,70,88,120,155]."""


list1=[12,24,35,70,88,120,155]
print([i for i in list1 if i%5!=0 and i%7!=0 ])
#
# removing_number=[]
#
# for i in list1:
# 	if i%7!=0 and i%5!=0:
# 		removing_number.append(i)
#
# print(removing_number)