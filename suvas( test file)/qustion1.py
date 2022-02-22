# Write a function to extract words from the sentence that are repeated multiple times, the
# function must return value(s). Display those words with ‘#’ separator (use join function).
# For example : WORD1 # WORD2 # WORD3


# def func(a):
# 	a = a.split()
# 	l1=[]
# 	l2=[]
# 	[l1.append(i) if i not in l1 else l2.append(i) for i in a]
# 	return l2
# a="hey u how are u hey hey ..."
# l2=func(a)
# print("#".join(l2))


# x={'a':{'b':[1,2,(3,4,{'c':3,'d':4,'e':[1,2,3]})]}}
#
#
# def func(das):
#     for k,v in das.items():
#         if k=='e':
#             print(k, ':', v[1])
#         if type(v)==dict:
#             func(v)
#         if type(v)==list:
#             for i in v:
#                 if type(i)==dict:
#                     func(i)
#                 if type(i)==tuple:
#                     for j in i:
#                         if type(j)==dict:
#                             func(j)
# func(x)


# x=[1,2,(3,4,5,{'a':1,'b':[2,3,4,(5,6)]})]


y = []
def func(das):

    for i in das:
        if type(i) == tuple:

            for j in i:
                if j == 6:
                    y.append(j)
                if type(j) == dict:
                    for n,m in j.items():
                        if type(m)==list:
                            func(m)
                    return y

x = [1, 2, (3, 4, 5, {'a': 1, 'b': [2, 3, 4, (5, 6)]})]
func(x)
print(y)
