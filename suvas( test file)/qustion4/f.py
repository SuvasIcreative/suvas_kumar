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


# f. Check company has any employee who has less than 2 years of experience.

emp_less_list = []


def less_exp(das):
    for k, v in das.items():
        if type(v) == dict:
            less_exp(v)
        elif type(v) == list:
            for j in v:
                if type(j) == dict:
                    less_exp(j)
                elif v[1] == None:
                    pass
                elif v[1] < 2:
                    emp_less_list.append(k)


less_exp(dicionary)
print(set(emp_less_list))
