list1=[1,2,3,4,5,6,7,8,9,10]
newlist=filter(lambda x:( x%2==0),list1)
print(list(newlist))