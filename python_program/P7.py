"""7). Write a program that computes the value of a+aa+aaa+aaaa 
with a given digit as the value of a.
Suppose the following input is supplied to the program:
9
Then, the output should be:
11106"""



number=int(input("How many time do want to write: "))
num=input("Enter a number:")
print(type(num))

result=0

for i in range(1 , number+1):
  result = result + int(num*i)
  #num * i
  print(num*i)

print(result)
