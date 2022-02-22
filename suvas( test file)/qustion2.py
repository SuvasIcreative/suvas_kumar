# 2. Write a program to extract string elements from a list based on below conditions, use
# in-built functions.
# a. First character must capitalize and consonant.
# b. String must not contain any number.


l1 = ['Ram', 'Sad', 'man', 'Arn', 'Sarsa', '1111']
l2 = ['A', 'E', 'I', 'O', 'U']
y = (list(filter(lambda i: i.isdigit() == True, l1)))
new_list = list(filter(lambda x: x[0] not in l2 and x[0].isupper() and x not in y, l1))

print(new_list)

x = {'ram': 5, 'sam': 10, 'raj': {'sem': 50}}


def func(das):
    for k, v in das.items():
        if type(v) == dict:
            func(v)
        else:
            if v % 2 == 0:
                print(k)




func(x)
