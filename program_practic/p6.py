l=[2,5,7,1,5,8,2,6,5,2,5]

#newlist=map(filter(i%2==0,l(lambda i: i*i),l)
#print(newlist)
#print(list(sorted(newlist)))



newlist=filter(lambda i:(i%2==0),l)
newlist1=map(lambda x:x*x,newlist)
print(list(sorted(newlist1)))