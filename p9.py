# # # # # # (h_letters) = [ letter for letter in 'human' ]
# # # # # # print( h_letters)


# # # # # num_list = [y for y in range(100) if y % 2 == 0 if y % 5 == 0]
# # # # # print(num_list)


# # # # obj = ["Even" if i%2==0 else "Odd" for i in range(10)]
# # # # print(obj)


# # # transposed = []
# # # matrix = [[1, 2, 3, 4], [4, 5, 6, 8]]

# # # for i in range(len(matrix)):
	
# # #     transposed_row = []

# # #     for row in matrix:
# # #         transposed_row.append(row[i])
# # #         print(row[i])
# # #     transposed.append(transposed_row)

# # # print(transposed)


# # matrix = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]
  
# # # # # Nested List Comprehension to flatten a given 2-D matrix
# # flatten_matrix = [val for sublist in matrix for val in sublist if val%2==0 ]
  
# # print(flatten_matrix)



# # matrix = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]
  
# # # flatten_matrix = []
  
# # # # for sublist in matrix:
# # # #     for val in sublist:
# # # #     	if val%2==0:
# # # #         	flatten_matrix.append(val)
          
# # # # print(flatten_matrix)



# # # [[flatten_matrix.append(val) for val in sublist if val%2==0] for sublist in matrix ]
# # # print(flatten_matrix)
# # x=[]
# # x=[x.append(val) for sublist in matrix for val in sublist if val%2==0]
# # print(x)



# # planets = [['Mercury', 'Venus', 'Earth'], ['Mars', 'Jupiter', 'Saturn'], ['Uranus', 'Neptune', 'Pluto']]
  
# # flatten_planets = []
  
# # for sublist in planets:
# #     for planet in sublist:
          
# #         if len(planet) < 6:
# #             flatten_planets.append(planet)
          
# # print(flatten_planets)






# # planets = [['Mercury', 'Venus', 'Earth'], ['Mars', 'Jupiter', 'Saturn'], ['Uranus', 'Neptune', 'Pluto']]
  
# # # Nested List comprehension with an if condition
# # flatten_planets = [planet for sublist in planets for planet in sublist if len(planet) < 6]
          
# # print(flatten_planets)


# matrix = [(1,(5,6), 2, 3), (4,5), [6, 7, 8, 9]]
# x=[v for sl in matrix for v in sl if v%2==0 and v%3==0]
# print(x)




# dict1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
# # Double each value in the dictionary
# double_dict1 = {k*2:v*3 for (k,v) in dict1.items() if v%2==0}
# print(double_dict1)




# new_dict_comp = {n*n:n**2 for n in range(10) if n%2 == 0}

# print(new_dict_comp)






# fahrenheit = {'t1':-30, 't2':-20, 't3':-10, 't4':0}

# #Get the corresponding `celsius` values
# celsius = list(map(lambda x: x*x, fahrenheit.values()))

# #Create the `celsius` dictionary
# celsius_dict = dict(zip(fahrenheit.keys(), celsius))

# print(celsius_dict)




# nested_dict = {'first':{'a':1}, 'second':{'b':2}}
# float_dict = {outer_k: {float(inner_v) for (inner_k, inner_v) in outer_v.items()} for (outer_k, outer_v) in nested_dict.items()}
# print(float_dict)



