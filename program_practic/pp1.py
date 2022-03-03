# # def func(s):
# #     s = s.split()
# #     temp = []
# #     arr = []
# #     [temp.append(i) if i not in temp else arr.append(i) for i in s]
# #     return arr

# # s="abc abc abd abc abd xse"
# # arr=func(s)
# # print("#".join(tuple(arr)))



# l1=["Xyz","abc","Bcd ji","Ssd"]
# l2=['a','e','i','o','u','A','E','I','O','U']


# print(list(filter(lambda x:type(x)==str and x[0] not in l2 and x == x.capitalize(),l1)))


# l1=[1000,2000,3000,7000,5000]

# print(list(filter(lambda x:len(str(x))==4 and int(str(x)[0])%2 !=0 and int(str(x)[-1])%2 ==0 and (x%3==0 or x%7==0) ,l1)))




