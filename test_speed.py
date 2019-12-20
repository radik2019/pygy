



import itertools


def perm(lst, da, a):
    lst2 = []

    for i in range(1, len(lst) + 1):

        for i in list(itertools.combinations(lst,i)):
            if da < sum(i) < a:
                if i not in lst2:
                    lst2.append(i)
    for i in lst2:
        print(sum(i), '==', i)
    return


lst = [222.14, 222.14, 222.14, 372.5, 312.4,
       252.2, 459.7, 459.7, 372.5]

#19.4

perm(lst,2100, 2190)








