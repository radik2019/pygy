import itertools

def prop():
    def string_to_list(s):
        lst = s.split()
        try:

            lst = [float(lst[i]) for i in range(len(lst))]
        except ValueError:
            return ('deve contenere solo numeri naturali '
                    'e razionali usando il punto al posto della virgola '
                    )
        return lst

    def prop_n(lst, n):
        a = 0
        ls = []
        for i in range(len(lst )+1):
            ab = itertools.combinations(lst, i)
            for k in ab:
                if sum(k) > a and sum(k) <= n:
                    a = sum(k)
                    ls = k
                else:
                    pass
        return ls

    index_n = 1
    def choice_list(sottopezzi, pezzi, index_n):

        for i in pezzi:
            lst.append(prop_n(sottopezzi, i))
            sum_list.append(i - sum(prop_n(sottopezzi, i)))
        #print(sum_list)
        ind = sum_list.index(min(sum_list))

     
        df[f'{index_n}) {pezzi.pop(ind)}'] = lst[ind]

        for i in lst[ind]:

            sottopezzi.remove(i)
        return


    sottopezzi = string_to_list(input('inserisci i pezzi pronti:\t'))
    pezzi = string_to_list(input('inserisci i pezzi da dividere:\t'))
    df = {}
    while len(sottopezzi) > 0 and len(pezzi) > 0:
        lst = []
        sum_list = []
        choice_list(sottopezzi, pezzi, index_n)
        index_n += 1

    for i in df:
        print('_' * 50)
        # print(f'{i} -- {df[i]}\nresto -- {i - sum(df[i])}')
        print(f'{i} -- {sum(df[i])} = {df[i]}')
    print('_' * 50)
    print(f'manca materiale per: {sottopezzi}')
    print(f'sono avanzati {sum(pezzi)}')

print(prop())


