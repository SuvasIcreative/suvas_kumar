"""24). With two given lists [1,3,6,78,35,55] and [12,24,35,24,88,120,155],
 write a program to make a list whose elements are intersection of the above given lists."""

list1 = [1, 3, 6, 78, 35, 55]
list2 = [12, 24, 35, 24, 88, 120, 155]

intersect = list(set(list1) & set(list2))
print(intersect)
