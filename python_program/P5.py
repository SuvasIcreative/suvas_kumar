"""5). Write a program that accepts sequence of lines as input and prints
 the lines after making all characters in the sentence capitalized.
Suppose the following input is supplied to the program:
Hello world
Practice makes perfect
Then, the output should be:
HELLO WORLD
PRACTICE MAKES PERFECT"""



no_of_lines = int(input("Enter numbr of line u want to write: "))
lines = ""

for i in range(no_of_lines):
    lines += input()+"\n"

print(lines.upper())