def prop_cut(free_list, fix_list):
    import itertools
    bst = []

    def perm(lst, a):
        lst2 = []
        da = 0
        for i in range(1, len(lst) + 1):
            for i in list(itertools.combinations(lst, i)):
                if da < sum(i) < a:
                    if i not in lst2:
                        lst2.append(i)
        max_sum = []
        for i in lst2:
            if sum(i) > sum(max_sum):
                max_sum = i
        return max_sum

    def sort_byrest(fix_list, free_list):
        dz1 = {}
        s2 = []
        free_list1 = free_list.copy()
        for k in range(len(free_list)):
            diz = {}
            slov = []
            for i in free_list1:
                a = (perm(fix_list, i))
                rest1 = i - sum(a)
                slov.append([rest1, i, a])
                diz[rest1] = a
            m = min(diz)
            m1 = min(slov)
            s2.append(m1)
            dz1[free_list[k]] = diz[m]
            for i in diz[m]:
                fix_list.remove(i)
            free_list1.remove(m1[1])
        return s2

    df = sort_byrest(fix_list, free_list)
    print()
    for i in df:
        print('_' * 50)
        print()
        print(f'il pezzo intero ====== {i[1]}')
        print(f'i pezzi da tagliare == {i[2]}')
        print(f'pezzi rimanenti======= {i[0]}')
        print('_' * 50)
    print('rimangono:  ', fix_list)
    return


def string_to_list(s):
    lst = s.split()
    try:

        lst = [float(lst[i]) for i in range(len(lst))]
    except ValueError:
        return ('deve contenere solo numeri naturali '
                'e razionali usando il punto al posto della virgola '
                )
    return lst

fx = input('inserisci i pezzi pronti:\t')
fr = input('inserisci i pezzi da dividere:\t')


fix_list = string_to_list(fx)
free_list = string_to_list(fr)
if type(fix_list) and type(free_list) is list:
    prop_cut(free_list, fix_list)
else:
    print(fix_list)
    print(free_list)
