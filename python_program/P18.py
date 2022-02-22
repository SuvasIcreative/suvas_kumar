"""18). Please write a program to generate all sentences where 
the subject is in ["I", "You"] and verb is in ["Play", "Love"] 
and the object is in [“Hockey”,”Football”]	"""



subjects=["I", "You"]
verbs=["Play", "Love"]
objects=["Hockey","Football"]
for i in subjects:
    for j in verbs:
        for k in objects:
            print (i,j,k)