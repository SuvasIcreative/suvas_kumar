
a = [1,2,3]

b = {
	1: [4,5,6],
	2: [7,8],
	3: [9, 10],
	4: [11, 12, 13],
	9: [14, 15],
	10: [16],
	13: [19, 20],
	19: [21]
}


# Output: [1, 4, 11, 12, 13, 19, 21, 20, 5, 6, 2, 7, 8, 3, 9, 14, 15, 10, 16]

l1=[]

def func(c):
	for i in c:
		for k,v in b.items():
			if i==k:
				l1.append(i)
				x=b.get(i)
				func(x)
		l1.append(i)

func(a)
print(list(dict.fromkeys(l1)))














