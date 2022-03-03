# # # # x = {'ram': 5, 'sam': 10, 'raj': {'sem': 50}}


# # # # def func(das):
# # # #     for k, v in das.items():
           
# # # #         if type(v) == dict:
# # # #             func(v)

# # # #             # if v % 2 == 0:
# # # #             #     print(k)
# # # #         else:
# # # #             if v % 2 == 0:
# # # #                 print(k)

        

# # # # func(x)




# # # # Python code to merge dict using update() method
# # # def Merge(dict1, dict2):
# # #     return(dict2.update(dict1))
     
# # # # Driver code
# # # dict1 = {'a': 10, 'b': 8}
# # # dict2 = {'d': 6, 'c': 4}
 
# # # # This return None
# # # (Merge(dict1, dict2))
 
# # # # changes made in dict2
# # # print(dict2)
# # # #print(dict1)

# # import random

# # a=[1,2,3,4,5,]
# # b=[6,7,8,9,10]
# # random.shuffle(b)
# # c=list(map(lambda x,y:x+y,a,b))
# # print(c)



# # x={'a':1,'b':2,'c':3,'d':[1,2,3,4,(5,6,7,{'e':5})]}

# # def func(das):
# #     for k,v in das.items():
# #         if k=='e':
# #             print(v)
# #         if type(v)==dict:
# #             func(v)
# #         if type(v)==list:
# #             for i in v:
# #                 if type(i)==dict:
# #                     func(i)
# #                 if type(i)==tuple:
# #                     for j in i:
# #                         if type(j)==dict:
# #                             func(j)
# # func(x)


# # x={'a':{'b':[1,2,(3,4,{'c':3,'d':4,'e':[1,2,3]})]}}


# # def func(das):
# #     for k,v in das.items():
# #         if k=='e':
# #             print(k,':',v[1])
# #         if type(v)==dict:
# #             func(v)
            
# #         if type(v)==list:
# #             for i in v:
# #                 if type(i)==dict:
# #                     func(i)
# #                 if type(i)==tuple:
# #                     for j in i:
# #                         if type(j)==dict:
# #                             func(j)
# # func(x)





# x=[1,2,(3,4,5,{'a':1,'b':[2,3,4,(5,6)]})]
# y=[]
# def func(das):
#     for i in das:
#         if type(i)==tuple:
           
#             for j in i:
#                 if j==6:
#                     print(j)  
#                 if type(j)==dict:
#                     for n,m in j.items():
#                         if type(m)==list:
#                             func(m)
#                     return y
# (func(x))
# # print(y)


# l1=[1,2,3,4,5]
# l2=[2,3,5,6,5]
# l3=zip(l1,l2)
# print(dict(l3))
# a,b=(zip(*l3))
# print(a,b)



# l1=[2,3,4,5,6,7,8,9,1]
# # def func(x):
# #     it=iter(x)
# #     new=dict(zip(it,it))
# #     return new
# # print(func(l1))

# l2=map(lambda x:x*x,l1)
# l3=dict(zip(l1,l2))
# print(l3)



# import random 

# l1=(random.sample(range(2,20),5))
# l2=dict(zip(l1,l1))
# print(l2)


a=[1,5,3,4]
b=['a','b','c','d']

x=map(lambda x,y:y*x,a,b)
print(list(x))
 
