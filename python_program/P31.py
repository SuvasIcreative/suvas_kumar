#31). Write a program to print the below pattern




n=5#int(input("Enter number"))
for i in range(n-1,-1,-1):
  for j in range(n-i-1):
    print("   ", end="")
  for j in range(i+1):
    print(" * ", end="")

  print( )