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


# a. Display all employees' names for the given project manager name.
# b. Display name of only those employees’ whose experience is more than 4 years.
# c. Update years of experience with 4.6 whose experience is greater than 3.5 and
# less than 4.5 year.
# d. Display TL with their year of experience, if has no experience then display N/A.
# e. Smith left the company and all his members were assigned to Ryan.
# f. Check company has any employee who has less than 2 years of experience.
# g. Check Edge is TL or not if not make him TL.

#(a)
dictionary ={}
dic_v = []
def rec_dict(dic):
    v = []
    for i,k in dic.items():
        if type(k) == dict:
            rec_dict(k)
        else:
            if :
                v.append(k)
    dic_v.extend(v)

rec_dict(dictionary)

print(dic_v)




#(B)

dictionary ={}
dic_v = []
def rec_dict(dic):
    val = []
    for i,k in dic.items():
        if type(k) == dict:
            rec_dict(k)
        else:
            if i>4:
                v.append(k)
    dic_v.extend(v)

rec_dict(dictionary)

print(dic_v)

#(c)
dictionary ={}
dic_v = []
def rec_dict(dic):
    val = []
    for i,k in dic.items():
        if type(k) == dict:
            rec_dict(k)
        else:
            if i>3.5 and i<4.5:
                v.append(k)
    dic_v.extend(v)

rec_dict(dictionary)

updated_dic_v=[i+4.6 for i in dic_v]

print(updated_dic_v)


(d)







