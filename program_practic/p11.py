# def _finditem(obj, key):
#     if key in obj: return obj[key]
#     for k, v in obj.items():
#         if isinstance(v,dict):
#             _finditem(v, key)

# s=_finditem({"B":{"A":2}},"A")
# print(s)








# no_of_lines = int(input("Enter numbr of line u want to write: "))
# lines = ""

# for i in range(no_of_lines):
#     lines+=input()+"\n"

# print(lines.upper())




x = (4,4,5,2,3,6,54,2,54,5)
y=(5,2,3,5)
n=dict(zip(y,x))
#thisdict =list(dict.fromkeys(x,y))


print((n))


