# n = int(input("Enter a number: "))
# #initialize the sum
# s = 0
# t = n
# while t > 0:
#    digit = t % 10
#    s += digit ** 3
#    t //= 10
# # display the result
# if n == s:
#    print(n,"is an Armstrong number")
# else:
#    print(n,"is not an Armstrong number")


# print([]*3)

# a=('a','b','c')*2
# print(a)

# print((2)**2)

# print([{}]*2)
#
# z=['p','l','j']
# z+='se'
# print(z)



a=[5,3,6,7,8,10]
print(list(map(lambda x:((x*a[-1])/100)+x,a)))







# for i in range(0,len(a)):
# 	a[i]=a[i]*a[i]
# print(a)
