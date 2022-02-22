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

# e. Smith left the company and all his members were assigned to Ryan.
x = []


def rec_upd_dict(das):
    for k, v in das.items():
        if k == 'Smith':
            x.append(v[2])
        if type(v) == dict:
            rec_upd_dict(v)
        if type(v) == list:
            for i in v:
                if type(i) == dict:
                    rec_upd_dict(i)


rec_upd_dict(dicionary)


# print(dicionary)
# print(x)

def rec_upd_dict(das):
    for k, v in das.items():
        if k == 'Ryan':
            v.extend(x)
        if type(v) == dict:
            rec_upd_dict(v)
        if type(v) == list:
            for i in v:
                if type(i) == dict:
                    rec_upd_dict(i)


rec_upd_dict(dicionary)
dicionary['Anne'].pop('Smith')
print(dicionary)
