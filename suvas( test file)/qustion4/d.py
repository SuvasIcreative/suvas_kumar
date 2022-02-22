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

# d. Display TL with their year of experience, if has no experience then display N/A.


def dpl_tl(dic):
    for k, v in dic.items():
        if type(v) == dict:
            dpl_tl(v)
        else:
            type(v) == list

            if v[0] == 'TL' and v[1] == None:
                print(k, ': N/a')
            elif v[0] == 'TL':
                print(k, ':', v[1])
            for i in v:

                if type(i) == dict:
                    dpl_tl(i)


dpl_tl(dicionary)
