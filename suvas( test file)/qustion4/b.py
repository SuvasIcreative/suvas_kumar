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

# b. Display name of only those employees’ whose experience is more than 4 years.

list_of_emp = []


def emp_sort_by_experience(das):
    for k, v in das.items():
        if type(v) == dict:
            emp_sort_by_experience(v)
        else:
            type(v) == list
            if v[1] == None:
                pass
            elif v[1] > 4:
                list_of_emp.append(k)

                for i in v:
                    if type(i) == list:
                        if i[1] == None:
                            pass
                        elif i[1] > 4:
                            list_of_emp.append(k)
                    elif type(i) == dict:
                        emp_sort_by_experience(i)


emp_sort_by_experience(dicionary)
print(list_of_emp)
