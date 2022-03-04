
# in the list of 0 index value is percentage of sale price

d = {'s1': {'p1': {'jan': [20,10, 30, 45, 50], 'feb': [30, 60, 64, 68]},

            'p2': {'jan': [20, 66, 67, 81, 75], 'feb': [30, 78, 81, 85]},

            'p3': {'jan': [35, 18, 20], 'feb': [40, 21, 22], 'mar': [50,22, 23, 24]}
            },
     's2': {'P1': {'jan': [10,206, 220, 225], 'mar': [15, 280, 300, 385], 'apr': [10, 160, 150, 136]},
            'p3': {},
            'p4': {'jan': [10, 300], 'feb': [10, 280, 300, 385], 'mar': [15, 280, 300, 385], 'apr': [10,360, 376]},
            'p6': {}
            },
     's3': {'p2': {'mar': [None, 55, 59, 61], 'apr': [None, 53, 54, 55]},
            'p4': {},
            'p6': {}}
     }
# a:
# def func(das):
#     for k, v in das.items():
#         if type(v) == dict:
#             func(v)
#         if type(v) == list:
#             if v[0]==None:
#                 pass
#             else:
#                 for i in range(1, len(v)):
#                     v[i] = ((v[i] * v[0]) / 100) + v[i]
#                     if type(i) == dict:
#                         func(i)
#                         return
# func(d)
# print(d)


# e:

# def func_to_reset_price(das):
#     for k, v in das.items():
#         if type(v) == dict:
#             func_to_reset_price(v)
#         if type(v) == list:
#             if v[0]==None:
#                 for i in range(1, len(v)):
#                     v[i] = (v[i] * 0)
#
#             else:
#                 for i in range(1, len(v)):
#                     v[i] = (v[i] * 0)
#                     if type(i) == dict:
#                         func_to_reset_price(i)
#                         return
# func_to_reset_price(d)
# print(d)



#d:
# d['s4']='p1'
# print(d)



l = []
def func(das):
    for k,v in das.items():

        if type(v)==dict:
            l.append(k)
            print(l)
            func(v)
        if type(v)==list:
            v[0]=int(input("Enter parcentage fpr {} in {} moths".format(l[-1],k)))
            for i in range(1, len(v)):
                v[i] = ((v[i] * v[0]) / 100) + v[i]
            for i in v:
                if type(i)==dict:
                    func(i)
func(d['s1'])
print(d)
