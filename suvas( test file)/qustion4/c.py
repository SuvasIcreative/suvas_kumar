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



# c. Update years of experience with 4.6 whose experience is greater than 3.5 and
# less than 4.5 year.


def rec_exp(dic):
    for k, v in dic.items():
        if type(v) == dict:
            rec_exp(v)
        else:
            type(v) == list
            for i in v:
                if type(i) == dict:
                    rec_exp(i)
                elif v[1] == None:
                    pass
                elif v[1] > 3.5 and v[1] < 4.5:
                    v[1] = (4.6)


rec_exp(dicionary)
print(dicionary)
