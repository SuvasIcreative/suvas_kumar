dicionary = {
    'Robert': {'Mark': ['TL', 8, {'Leonardo': ['JD', 1], 'Alexandra ': ['JD', 1]}],

               'Samuel': ['Tl', 8],

               'Paul': ['TL', 8, {'Fergal': ['SD', 4.5]}],

               'Tom': ['TL', 8, {'Jerry': ['JD', 1.5], 'John': ['JD', 1.6]}]
               },

    'Anne': {'Chris': ['TL', 5, {'James': ['TL', None, {'Jennifer': ['SD', 3.8], 'Scott': ['SD', 3.8],
                                                        'Sophie': ['SD', 3.8]}]}],
             'Pratt': ['TL', 5],

             'Emma': ['TL', 5],

             'Will': ['TL', 5, {'Edge': ['SD', 3], 'Ryan': ['SD', 3.5]}],

             'Smith': ['TL', 5, {'Walker': ['SD', 2.7], 'Diana ': ['SD', 2.7]}]
             }

}

# a. Display all employees' names for the given project manager name.


emp_list = []

def pm_emp_name(das):
    for k, v in das.items():
        if type(v) == dict:
            pm_emp_name(v)
            emp_list.append(k)

        if type(v) == list:
            emp_list.append(k)

            for i in v:
                if type(i) == dict:
                    pm_emp_name(i)
                    emp_list.append(k)
                if type(i) == list:
                    emp_list.append(k)
                    pm_emp_name(i)


pm_emp_name(dicionary['Robert'])
pm_emp_name(dicionary['Anne'])
print(set(emp_list))


# emp_list = []


# def pm_emp_name(das):
#     for k, v in das.items():
#         if type(v) == dict:
#             pm_emp_name(v)
#             if k != 'Robert' and k != 'Anne':
#                 emp_list.append(k)
#
#         if type(v) == list:
#             if k != 'Robert' and k != 'Anne':
#                 emp_list.append(k)
#
#         for i in v:
#             if type(i) == dict:
#                 pm_emp_name(i)
#                 if k != 'Robert' and k != 'Anne':
#                     emp_list.append(k)
#             if type(i) == list:
#                 if k != 'Robert' and k != 'Anne':
#                     emp_list.append(k)
#             pm_emp_name(i)
#
#
# #pm_emp_name(dicionary)
# pm_emp_name(dicionary['Anne'])
# print(set(emp_list))
