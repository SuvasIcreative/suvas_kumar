"""6). Write a program that accepts a sentence and calculate 
the number of uppercase letters and lowercase letters.
Suppose the following input is supplied to the program:
Hello world!
Then, the output should be:
UPPER CASE 1
LOWER CASE 9
"""


# no_of_lines = int(input("Enter numbr of line u want to write: "))
# lines = ""
# upper = 0
# lower = 0
#
# for i in no_of_lines:
#     lines += input()+"\n"
#
#
# print('Lower case letters= ', lower)
# print('Upper case letters=', upper)
#



no_of_lines = int(input("Enter numbr of line u want to write: "))
string = ""

for i in range(no_of_lines):
    string += input()+"\n"

count1=0
count2=0
for i in string:
      if(i.islower()):
            count1=count1+1
      elif(i.isupper()):
            count2=count2+1
print("The number of lowercase characters is:")
print(count1)
print("The number of uppercase characters is:")
print(count2)