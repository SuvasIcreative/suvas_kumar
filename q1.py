def fun(n):
    n = n.split()
    l1 = []
    l2 = []
    for i in n:
        if i not in l1:
            l1.append(i)
        else:
            l2.append(i)
    return l2


n = ("hey u how are u hey how")
l2 = fun(n)
print("##".join(l2))
