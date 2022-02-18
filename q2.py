list1 = ['ran', 'Ram', 'Sun', 'arm']
list2 = ['A',  'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u']

new_list = list(filter(lambda x: type(x) != int and x[0] not in list2 and x == x.capitalize(), list1))

print(new_list)
