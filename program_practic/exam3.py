# Write a program to create a list of numbers, extract integer numbers from a list based on
# below conditions.
# a. Number must be 4 digit long i.e (1000 to 9999)
# b. First digit of the number must be odd and the last digit must be even.
# c. Number must be divisible by either 3 or 7.


#(a)
# list1=[9998,555,34576,2435]
# x=[]
# count=0
# for i in list1:
# 	if len(str(i))==4:
# 		(x.append(i))
# print((x))


#(c)
list1=[9998,555,34576,2435]

new_list=[x for x in list1 if x%3!=0 and x%7!=0 ]
print(new_list)






 


