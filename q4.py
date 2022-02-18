# 4. In one company there are few employees (Prepare dictionary from below details):
# -
# Robert Downey and Anne Hathaway are Project Managers. Robert has 4 TL: Mark,
# Samuel, Paul and Tom, all have 8 Years of experience. Anne has 5 TLs, all have 5 Years
# of Experience: Chris, Pratt, Emma, Will and Smith. James is TL and has 3 senior
# developers Jennifer, Scott and Sophie, they have 3.8 years of experience and his
# manager is Chris, Fergal is senior developer and has 4.5 year of experience and his
# mentor is Paul. Edge has 3 years of experience and Ryan has 3.5 years of experience.
# Their designation is senior developer and his manager is Will. Jerry and John are junior
# developers and his mentor is Tom, their experience is 1.5 and 1.6 year of experience.
# Leonardo and Alexandra are junior developers and their mentor is Mark and has 1 year
# of experience of each. Walker and Diana are senior developers and they have 2.7 years
# of experience and their reporting manager is Smith.

details={'Robert': ['PM', {'TL': 4},{'Mark':['TL',8,{'Leonardo':['JD',1],'Alexandra':['JD',1]}],

                        'Samuel':['TL',8], 'Paul':['TL',8, {'Fergal':['SD',4.5]}] ,
                                            'Tom':['TL',8,{'Jerry':['JD',1.5],'Jone':['JD',1.6]}]}],

        'Anne ':['PM', {'TL':5}, {'Chris': ['TL',5,'M', {'James':['TL',None, {'SD':3},

                                             {'Jennifer':['SD',3.8], 'Scott':['SD',3.8] ,'Sophie':['SD',3.8]}]}],

             'Pratt':['TL',5], 'Emma':['TL',5], 'Will':['TL',5,'M',{'Edge':['SD',3],
                                                                    'Ryan':['SD',3.5],'Diana':['SD',2.7]}],
                                          'Smith':['Tl',5,'RM',{'Walker':['SD',2.7]}]}]
}


# a. Display all employees' names for the given project manager name.

employees=[]

def rec_dect(dic):

    for i in dic:
        if type(i)==list:
            for j in i:
                if type(j)==dict:
                    employees.extend(j.keys())
                    rec_dect(j.values)
        elif type(i) == dict:
            employees.extend(i.keys())


rec_dect(details['Robert'])
print(employees)

# x = details.items()
# print(x)


