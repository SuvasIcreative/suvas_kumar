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


dicionery={'Robert':['PM',None,{'Mark':['TL',8,{'Leonardo':['JD',1],'Alexandra':['JD',1]}],

							'Samuel':['TL',8],

							'Paul':['TL',8,{'Fergal':['SD',4.5]}],

							'Tom':['TL',8,{'Jerry':['JD',1.5],'Jone':['JD',1.6]}]}],

		'Anne':['PM',None,{'Chris':['TL',5,{'James':['TL',None,{'Jennifer':['SD',3.8],

																'Scott':['SD',3.8],

																'Sophie':['SD',3.8]}]}],

							'Pratt':['TL',5],

							'Emma':['TL',5],

							'Will':['TL',5,{'Edge':['SD',3],'Ryan':['SD',3.5]}],

							'Smith':['TL',5,{'Walker':['SD',2.7],'Diana':['sd',2.7]}]}]

}
# a. Display all employees' names for the given project manager name.

# emp_list = []


# def pm_emp_name(das):
#     for k, v in das.items():
#         if type(v) == dict:
#             pm_emp_name(v)
#             if k != 'Robert' and k != 'Anne':
#                 emp_list.append(k)

#         if type(v) == list:
#             if k != 'Robert' and k != 'Anne':
#         	    emp_list.append(k)

#         for i in v:
#             if type(i) == dict:
#                 pm_emp_name(i)
               


# pm_emp_name(dicionery)
# # pm_emp_name(dicionary['Anne'])
# print(set(emp_list))



# # b. Display name of only those employees’ whose experience is more than 4 years.
# epl_list=[]
# def dpl_by_exp(das):
# 	for k,v in das.items():
# 		if type(v)==dict:
# 			dpl_by_exp(v)
# 		elif type(v)==list:
# 			if v[1]==None:
# 				pass
# 			elif v[1]>4:
# 				epl_list.append(k)
# 			for i in v:
				
# 				if type(i)==dict:
# 					dpl_by_exp(i)					


# dpl_by_exp(dicionery)
# print(epl_list)


# c. Update years of experience with 4.6 whose experience is greater than 3.5 and
# less than 4.5 year.

# epl_list=[]
# def dpl_by_exp(das):
# 	for k,v in das.items():
# 		if type(v)==dict:
# 			dpl_by_exp(v)
# 		if type(v)==list:
# 			if v[1]==None:
# 				pass
# 			elif v[1]>=3.5 and v[1]<=4.5:
# 				v[1]=4.6
# 			for i in v:
				
# 				if type(i)==dict:
# 					dpl_by_exp(i)


# dpl_by_exp(dicionery)
# print(dicionery)

# d. Display TL with their year of experience, if has no experience then display N/A.

# #epl_list=[]
# def dpl_by_exp(das):
# 	for k,v in das.items():
# 		if type(v)==dict:
# 			dpl_by_exp(v)
# 		if type(v)==list:
# 			if v[0]=='TL' and v[1]==None:
# 				print(k,': N/a')
# 			elif v[0]=='TL':
# 				print(k,':',v[1])
# 			for i in v:
				
# 				if type(i)==dict:
# 					dpl_by_exp(i)
					


# dpl_by_exp(dicionery)
# # #print(dicionery)



# e. Smith left the company and all his members were assigned to Ryan.

# epl_list=[]
# def dpl_by_exp(das):
# 	for k,v in das.items():
# 		if type(v)==dict:
# 			if k=='Smith':
# 				epl_list.append(v[2])
# 			dpl_by_exp(v)
# 		if type(v)==list:
# 			for i in v:				
# 				if type(i)==dict:
# 					if k=='Smith':
# 						epl_list.append(v[2])
# 					dpl_by_exp(i)

# dpl_by_exp(dicionery)
# (dicionery['Anne'][2]).pop('Smith')
# print(epl_list)

# def dpl_by_exp(das):
# 	for k,v in das.items():
# 		if k=='Ryan':
# 			v.extend(epl_list)
# 		if type(v)==dict:	
			
# 			dpl_by_exp(v)
# 		if type(v)==list:
# 			for i in v:								
# 				if type(i)==dict:					
# 					dpl_by_exp(i)	


# dpl_by_exp(dicionery)
# print(dicionery)





# f. Check company has any employee who has less than 2 years of experience.



# epl_list=[]
# def dpl_by_exp(das):
# 	for k,v in das.items():
# 		if type(v)==dict:
# 			dpl_by_exp(v)
# 		if type(v)==list:
# 			if v[1]==None:
# 				pass
# 			elif v[1]<2:
# 				print(k)
# 			for i in v:
				
# 				if type(i)==dict:
# 					dpl_by_exp(i)


# dpl_by_exp(dicionery)


# g. Check Edge is TL or not if not make him TL.



# def dpl_by_exp(das):
# 	for k,v in das.items():
# 		if k=='Edge':
# 			if v[0]!='TL':
# 				v[0]='TL'

# 		if type(v)==dict:	
			
# 			dpl_by_exp(v)
# 		if type(v)==list:
# 			for i in v:								
# 				if type(i)==dict:					
# 					dpl_by_exp(i)	


# dpl_by_exp(dicionery)
# print(dicionery)

# def dpl_by_exp(das):
# 	for k,v in das.items():
		
# 		if type(v)==dict:
# 			dpl_by_exp(v)
# 		if type(v)==list:
# 			if v[1]==None:
# 				print(k)
# 			for i in v:								
# 				if type(i)==dict:					
# 					dpl_by_exp(i)	


# dpl_by_exp(dicionery)
# #print(dicionery)


# def dpl_by_exp(das):
# 	for k,v in das.items():
		
# 		if type(v)==dict:
# 			print(k,':',V[1])
# 			dpl_by_exp(v)
# 		if type(v)==list:
# 				print(k,':',v[1])
# 		for i in v:								
# 			if type(i)==dict:					
# 				dpl_by_exp(i)	


# dpl_by_exp(dicionery)