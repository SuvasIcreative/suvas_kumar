# a=1523
# l=[]
# def fun(c):
# 	for i in c:
# 		l.append((int(i))**3)
# 	if (sum(l))==a:
# 		print("Yes")
# 	else:
# 		print("No")
# fun(str(a))



# a=['ram','sya&m','Raju','aman','ram1']
# b=('a','e','i','o','u')
# s= "!@#$%^&*()-+?_=,<>/"
# n=list(filter(lambda x:x[0] not in b and not any(i.isdigit() for i in x) and x[0].islower() 
# 	and not any(j in s for j in x),a))
# print(n)


# a=[4533,2,222,3545,224523,8532,4550]
# n=list(filter(lambda x:x in range(1000,9999) and int(str(x)[1])%2!=0 
# 	and int(str(x)[-1])%2==0 and (x%8==0 or x%5==0),a))
# print(n)


a=[5,6,4,7]
a[0]=int(input("Enter"))
# for i in a:
# 	a.append(i)
print(a)