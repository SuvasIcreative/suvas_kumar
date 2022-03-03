# 1. Write a function to extract words from the sentence that are repeated multiple times, the
# function must return value(s). Display those words with ‘#’ separator (use join function).
# For example : WORD1 # WORD2 # WORD3

def func(s):
	s=s.split()
	temp=[]
	arr=[]
	[temp.append(i) if i not in temp else arr.append(i) for i in s]	
	return arr

s="aa bb aa bb "
arr=func(s)
#print((arr))
print("#".join(tuple(arr)))


# def func(s):
#     s = s.split()
#     temp = []
#     arr = []
#     [temp.append(i) if i not in temp else arr.append(i) for i in s]
#     return arr

# s="abc abc abd abc abd xse"
# arr=func(s)
# print("#".join(tuple(arr)))