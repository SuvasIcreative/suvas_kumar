# # Write a function to extract words from the sentence that are repeated multiple times, the
# # function must return value(s). Display those words with ‘#’ separator (use join function).
# # For example : WORD1 # WORD2 # WORD3


# def func(a):
# 	a=a.split()
# 	l1=[]
# 	l2=[]
# 	[l1.append(i) if i not in l1 else l2.append(i) for i in a]
# 	return l2
# a="hey u how are u hey"
# l2=func(a)
# print("#".join(l2))



# 2. Write a program to extract string elements from a list based on below conditions, use
# in-built functions.
# a. First character must capitalize and consonant.
# b. String must not contain any number.


# l1=['Ram','Sad','man','Arn','Sarsa']
# l2=['A','E','I','O','U','a','e','i','o','u']
# new_list=list(filter(lambda x: x[0] not in l2 and len(x)==5  and x[-1] in l2 and type(x)!=int and
#  x==x.capitalize()  ,l1))
# print((new_list))


# 3. Write a program to create a list of numbers, extract integer numbers from a list based on
# below conditions.
# a. Number must be 4 digit long i.e (1000 to 9999)
# b. First digit of the number must be odd and the last digit must be even.
# c. Number must be divisible by either 3 or 7.


# list1=[4254,5564,4861,8875,6935,556,5456665]

# new_list=filter(lambda x: len(str(x))==4 and int(str(x)[0])%2==0
#  and x%2==0 and (x%3==0 or x%7==0) ,list1)

# print(list(new_list))



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





dicionary={
			'Robert':{'Mark':['TL',8,{'Leonardo':['JD',1],'Alexandra ':['JD',1]}],

					'Samuel':['Tl',8],

					'Paul':['TL',8,{'Fergal':['SD',4.5]}],

					'Tom':['TL',8,{'Jerry':['JD',1.5],'John':['JD',1.6]}]
			},

		'Anne':{'Chris':['TL',5,{'James': ['TL',None,{'Jennifer':['SD',3.8],'Scott':['SD',3.8],
															'Sophie':['SD',3.8]}]}],
					'Pratt':['TL',5],

					'Emma':['TL',5],

					'Will':['TL',5,{'Edge':['SD',3],'Ryan':['SD',3.5]}],

					'Smith':['TL',5,{'Walker':['SD',2.7],'Diana ':['SD',2.7]}]
		}	
	
}



# a. Display all employees' names for the given project manager name.


# emp_list=[]
# def pm_emp_name(das):

# 	for k,v in das.items():
# 		if type(v)==dict:
			
# 			pm_emp_name(v)
# 			emp_list.append(k)
			
# 		if type(v)==list:
# 			emp_list.append(k)
			
# 			for i in v:
# 				if type(i)==dict:
					
# 					pm_emp_name(i)
# 					emp_list.append(k)
# 				if type(i)==list:
# 					emp_list.append(k)
# 					pm_emp_name(i)
				


# pm_emp_name(dicionary['Robert'])
# pm_emp_name(dicionary['Anne'])
# print(set(emp_list))


# b. Display name of only those employees’ whose experience is more than 4 years.

# list_of_emp=[]
# def emp_sort_by_experience(das):
# 	for k,v in das.items():
# 		if type(v)==dict:
# 			emp_sort_by_experience(v)
# 		else:
# 			type(v)==list
# 			if v[1]==None:
# 				pass
# 			elif v[1] > 4:
# 				list_of_emp.append(k)
			
# 				for i in v :
# 					if type(i)==list:
# 						if i[1]==None:
# 							pass
# 						elif i[1] > 4:
# 							list_of_emp.append(k)
# 					elif type(i)==dict:
# 						emp_sort_by_experience(i)
				

# emp_sort_by_experience(dicionary)
# print(list_of_emp)




# c. Update years of experience with 4.6 whose experience is greater than 3.5 and
# less than 4.5 year.




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

# rec_exp(dicionary)
# print(dicionary)



# d. Display TL with their year of experience, if has no experience then display N/A.


# def dpl_tl(dic):
#     for k, v in dic.items():
#         if type(v) == dict:
#             dpl_tl(v)
#         else:
#             type(v) == list

#             if v[0] == 'TL' and v[1] == None:
#                 print(k, ': N/a')
#             elif v[0] == 'TL':
#                 print(k, ':', v[1])
#             for i in v:

#                 if type(i) == dict:
#                     dpl_tl(i)
                

# dpl_tl(dicionary)



# f. Check company has any employee who has less than 2 years of experience.

# emp_less_list = []
# def less_exp(das):
#     for k,v in das.items():
#         if type(v) == dict:
#             less_exp(v)
#         elif type(v) == list:
#             for j in v:
#                 if type(j) == dict:
#                     less_exp(j)
#                 elif v[1] == None:
#                     pass
#                 elif v[1] < 2:
#                     emp_less_list.append(k)
# less_exp(dicionary)
# print(set(emp_less_list))


# g. Check Edge is TL or not if not make him TL.


# def rec_chek(das):
# 	for k,v in das.items():
# 		if k == 'Edge' and v[0]!='TL':
# 			v[0]='TL'
# 		if type(v)==dict:
# 			rec_chek(v)
# 		if type(v)==list:
# 			for i in v:
# 				if type(i)==dict:
# 					rec_chek(i)
					
# rec_chek(dicionary)
# print(dicionary)


# # e. Smith left the company and all his members were assigned to Ryan.
# x=[]

# def rec_upd_dict(das):
# 	for k,v in das.items():
# 		if k=='Smith':
# 			x.append(v[2])
# 		if type(v)==dict:
# 			rec_upd_dict(v)
# 		if type(v)==list:
# 			for i in v:
# 				if type(i)==dict:
# 					rec_upd_dict(i)
# rec_upd_dict(dicionary)
# # print(dicionary)
# # print(x)

# def rec_upd_dict(das):
# 	for k,v in das.items():
# 		if k=='Ryan':
# 			v.extend(x)
# 		if type(v)==dict:
# 			rec_upd_dict(v)
# 		if type(v)==list:
# 			for i in v:
# 				if type(i)==dict:
# 					rec_upd_dict(i)

# rec_upd_dict(dicionary)
# dicionary['Anne'].pop('Smith')
# print(dicionary)


# def is_string_contain_number(f_s):
#     return len(list(filter(lambda ch: ch.isdigit()==True, f_s))) != 0


# def extract_valid_words(f_li):
#     f_li2 = []

#     for s in f_li:
#         if (s[0].isupper()) and (s[0] not in ('A', 'E', 'I', 'O', 'U')) and not is_string_contain_number(s):
#             f_li2.append(s)

#     return f_li2


# li = ["Python", "Python1", "python", "Java/", "java1", "Arav"]
# print(extract_valid_words(li))




# def chek_isdigit(das):
# 	return len(list(filter(lambda x:x.isdigit()==True,das)))!=0
# def chek_list(dash):
# 	list2=[]
# 	for  i in dash:
# 		if( i[0].isupper()) and (i[0] not in ('A','E','I','O','U')) and not  chek_isdigit(i):
# 			list2.append(i)
# 			#print(list2)
# 	return list2

# list1=['Hey','Aiou','amir','garib','Sad1',111]
# print(chek_list(list1))
# #print(list2)



def rec_list(x):
	if x.isinstance(x[0],list):
		for i in x:
			if i%2==0:
				l1.append(i)
	else:
		for i in x:
			if i%2==0:
				l1.append(i)

y = [[5],12,45,13,14.5,12.6,'65','78',[75,4,62,'42','def',[84,96,'42.2',False]]]
rec_list(y)
#print(l1)
