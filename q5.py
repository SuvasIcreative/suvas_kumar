dicionary = {
    'Robert': {
        'Mark': ['TL', 8, {'Leonardo': ['JD', 1],
                           'Alexandra': ['JD', 1]}],
        'Samuel': ['TL', 8],
        'Paul': ['TL', 8, {'Fergal': ['SD', 4.5]}],
        'Tom': ['TL', 8, {'Jerry': ['JD', 1.5],
                          'Jems': ['JD', 1.6]}]
    },

    'Anne': {
        'Chris': ['TL', 5, {'James': ['TL', None, {'Jenifer': ['SD', 3.8],
                                                   'Scott': ['SD', 3.8],
                                                   'SOphie': ['SD', 3.8]}]}],
        'Pratt': ['TL', 5],
        'Emma': ['TL', 5],
        'Will': ['TL', 5, {'Edge': ['SD', 3],
                           'Ryan': ['SD', 3.5]}],
        'Smith': ['TL', 5, {'Walker': ['SD', 2.7],
                            'Diana': ['SD', 2.7]}]
    }
}


# emp_list = []
# def rec_manager(dic):
#     emp_list.extend(dic.keys())
#     for i in dic.values():
#         if type(i) == list:
#             for j in i:
#                 if type(j) == dict:
#                     rec_manager(j)
#
# #Robert's Employee
# rec_manager(dicionary['Robert'])
# print("Robert's Employees :",emp_list,'\n')
#
# emp_list.clear()
# rec_manager(dicionary['Anne'])
# print("Robert's Employees :",emp_list,'\n')



#b.) Display name of only those employees’ whose experience is more than 4 years.
# exp_list = []
# def rec_exp(dic):
#     for k,v in dic.items():
#         if type(v)==dict:
#             rec_exp(v)
#         else:
#             type(v)==list
#             for i in v:
#                 if type(i)==dict:
#                     rec_exp(i)
#                 elif v[1]==None:
#                     pass
#                 elif v[1]>4:
#                     exp_list.append(k)
#
#
# rec_exp(dicionary)
# print(set(exp_list))


# c. Update years of experience with 4.6 whose experience is greater than 3.5 and
# less than 4.5 year.

# exp_list = []
# def rec_exp(dic):
#     for k,v in dic.items():
#         if type(v) == dict:
#             rec_exp(v)
#         else:
#             type(v) == list
#             for i in v:
#                 if type(i) == dict:
#                     rec_exp(i)
#                 elif v[1]==None:
#                     pass
#                 elif v[1]>3.5 and v[1]<4.5:
#                     v[1]=(4.6)
#
# rec_exp(dicionary)
# print(dicionary)



# d. Display TL with their year of experience, if has no experience then display N/A.

# def rec_dict(dic):
#     for k, v in dic.items():
#         if type(v) == dict:
#             rec_dict(v)
#         elif type(v) == list:
#             for i in v:
#                 if type(i)==dict:
#                     rec_dict(i)
#             if v[0]=='TL' and v[1]== None:
#                 print(k, ': N/a')
#             elif v[0] == 'TL':
#                 print(k, ':', v[1])
#
#
#
# rec_dict(dicionary)


# def dpl_tl(dic):
#     for k, v in dic.items():
#         if type(v) == dict:
#             dpl_tl(v)
#         else:
#             type(v) == list
#
#             if v[0] == 'TL' and v[1] == None:
#                 print(k, ': N/a')
#             elif v[0] == 'TL':
#                 print(k, ':', v[1])
#             for i in v:
#
#                 if type(i) == dict:
#                     dpl_tl(i)
#                 elif i[0] == 'TL' and i[1] == None:
#                     print(k, ': N/a')
#                 elif i[0] == 'TL':
#                     print(k, ':', i[1])
#
#
# dpl_tl(dicionary)


# (f)


emp_exp_list = []
def emp_less_exp(dic):
    for k,v in dic.items():
        if type(v) == dict:
            emp_less_exp(v)
        elif type(v) == list:
            for j in v:
                if type(j) == dict:
                    emp_less_exp(j)
                elif v[1] == None:
                    pass
                elif v[1] < 2:
                    emp_exp_list.append(k)
emp_less_exp(dicionary)
print(set(emp_exp_list))
print('\n')