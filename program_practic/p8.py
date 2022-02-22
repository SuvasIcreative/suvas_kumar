# # # # # # # # # # # # l1=[10,20,30,[40,50,[60,'asd']]]

# # # # # # # # # # def even(a):
# # # # # # # # # # # #     l2=[]
# # # # # # # # # # # #     for i in a:
# # # # # # # # # # # #         try:
# # # # # # # # # # # #             l2.append(float(i))
# # # # # # # # # # # #         except:
# # # # # # # # # # # #             try:
# # # # # # # # # # # #                 l2.extend(even(i))
# # # # # # # # # # # #             except:
# # # # # # # # # # # #                 pass
# # # # # # # # # # # #     return l2
# # # # # # # # # # # # print(even(l1))# # 


# # # # # # # # # # # # # # # # # # # def fun():
# # # # # # # # # # # # # # # # # # #   print("Welcome to GFG")
# # # # # # # # # # # # # # # # # # # fun()


# # # # # # # # # # # # # # # # # # def evenOdd(x):
# # # # # # # # # # # # # # # # # #     if (x % 2 == 0):
# # # # # # # # # # # # # # # # # #         print("even")
# # # # # # # # # # # # # # # # # #     else:
# # # # # # # # # # # # # # # # # #         print("odd")
 
 
# # # # # # # # # # # # # # # # # # # Driver code to call the function
# # # # # # # # # # # # # # # # # # evenOdd(5)
# # # # # # # # # # # # # # # # # # evenOdd(102)


# # # # # # # # # # # # # # # # # def appendItem(itemName, itemList = []):
# # # # # # # # # # # # # # # # #     itemList.append(itemName)
# # # # # # # # # # # # # # # # #     return itemList
 
 
# # # # # # # # # # # # # # # # # print(print(appendItem('notebook  ')))
# # # # # # # # # # # # # # # # # print(print(appendItem('pencil')))
# # # # # # # # # # # # # # # # # print(appendItem('eraser'))
# # # # # # # # # # # # # # # # # print(print(type(print)))


# # # # # # # # # # # # # # # # print('#list')
# # # # # # # # # # # # # # # # def appendItem(itemName, itemList=[]):
# # # # # # # # # # # # # # # #     #if itemList == None:
# # # # # # # # # # # # # # # #     itemList = []
# # # # # # # # # # # # # # # #     itemList.append(itemName)
# # # # # # # # # # # # # # # #     return itemList
 
 
# # # # # # # # # # # # # # # # print(appendItem('notebook'))
# # # # # # # # # # # # # # # # print(appendItem('pencil'))
# # # # # # # # # # # # # # # # print(appendItem('eraser'))

# # # # # # # # # # # # # # # def student(firstname, lastname):
# # # # # # # # # # # # # # #     print(firstname, lastname)
 
 
# # # # # # # # # # # # # # # # Keyword arguments
# # # # # # # # # # # # # # # student(firstname='Geeks', lastname='Practice')
# # # # # # # # # # # # # # # student(lastname='Practice', firstname='Geeks')

# # # # # # # # # # # # # # def myFun(*argv):
# # # # # # # # # # # # # #     for arg in argv:
# # # # # # # # # # # # # #         print(arg)
 
 
# # # # # # # # # # # # # # myFun('Hello', 'Welcome', 'to', 'GeeksforGeeks')



# # # # # # # # # # # # # def myFun(**kwargs):
# # # # # # # # # # # # #     for key, value in kwargs.items():
# # # # # # # # # # # # #         print("%s == %s" % (key, value))
 
 
# # # # # # # # # # # # # # Driver code
# # # # # # # # # # # # # myFun(first='Geek', mid='for', last='Geeks')



# # # # # # # # # # # # def my_function():
# # # # # # # # # # # #     '''Demonstrates triple double quotes
# # # # # # # # # # # #     docstrings and does nothing really.'''
# # # # # # # # # # # #     return None
  
# # # # # # # # # # # # print("Using __doc__:")
# # # # # # # # # # # # print(my_function.__doc__)
  
# # # # # # # # # # # # print("Using help:")
# # # # # # # # # # # # #help(my_function)






# # # # # # # # # # # def square_value(num):
# # # # # # # # # # #     """This function returns the square
# # # # # # # # # # #     value of the entered number"""
# # # # # # # # # # #     return num**4
 
 
# # # # # # # # # # # print(square_value(2))
# # # # # # # # # # # print(square_value(-4))



# # # # # # # # # # def myFun(x):
# # # # # # # # # #     x[0] = 20
# # # # # # # # # #     x[1]=50
    
# # # # # # # # # #     y=x[1]+x[5]
# # # # # # # # # #     x[4]=y
# # # # # # # # # #     return y

 
 
# # # # # # Driver Code (Note that lst is modified
# # # # # # after function call.
# # # # # lst = [10, 11, 12, 13, 14, 15]
# # # # # y=myFun(lst)
# # # # # print(lst)
# # # # # print(y)





# # # # # # # # # def cube(x): return x*x*x
 
# # # # # # # # # cube_v2 = lambda x : x*x*x
 
# # # # # # # # # print(cube(6))
# # # # # # # # # print(cube(7))



# # # # # # # # tables = [lambda x=x: x*10 for x in range(1, 11)]
# # # # # # # # print(list(list(tables)))
 
# # # # # # # # for table in tables:
# # # # # # # #     print(table())


 
# # # # # # # def f1():
# # # # # # #     print(s)
# # # # # # #     def f2():

# # # # # # #         s = 'I love GeeksforGeeks'

         
# # # # # # #     f2()
 
# # # # # # # # Driver's code
# # # # # # # f1()




# # # # # # def myFun(arg1, arg2, arg3, arg4) :
# # # # # #     print("arg1:", arg1)
# # # # # #     print("arg2:", arg2)
# # # # # #     print("arg3:", arg3)
# # # # # #     print("arg4:", arg4) 
# # # # # # args = ("My", "name", "is","Vishal")
# # # # # # myFun(*args)



# # # # def myFun(name, *args):
# # # #     print(name)
# # # #     if args:
# # # #         print(list(args))
# # # # myFun("Vishal") #name parameter passed
# # # # myFun("Vishal",1,2,3)



# # # def fun(*args):
# # #     args=args + (4,5,100000)
# # #     return args

# # # print(fun(1,2,3))



# # def myFun(name, **kwargs):
# #     print(name)
# #     if kwargs:
# #         print(kwargs)
# # myFun("Vishal") #name parameter passed
# # myFun("Vishal",one=1,two=2,three=3)


# def fun(**kwargs):
#     kwargs['name']='Vishal'
#     print(kwargs)
#     return kwargs
# fun(roll=12, subject='Data Science')




# def fun(a,b,c):
#     return a+b+c
# x=fun(2,4,4)
# print(x)    



# def fun(a,b,c):
#     print(colore)
#     print( a,b,c)
# colore=('red','blue','green')
# fun(*colore)


# def mul(a,*args):
#     print(a*sum(args))
#     print(a)
#     # result=1
#     # for i in args:
#     #     result=i*result
#     # print(result)
# mul(2,3,4,5)
# mul(4,5,5,4,6,0,5)


# def mul(**d):
#     print(a+b+c)
# f={'a':2,"b":5,'c':10}
# mul(f)

d = {'key1': 1,'key2': 14,'key3': 47}

print(sum(d.values()))
 print(sum)