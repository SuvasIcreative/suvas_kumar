list1 = [4124, 5454, 34587, 124, 4878, 5365]

new_list = list(filter(lambda x: len(str(x)) == 4 and
            int(str(x)[0]) % 2 != 0 and x % 2 == 0 and (x % 3 == 0 or x % 7 ==0), list1))

print(new_list)