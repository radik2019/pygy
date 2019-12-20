

def decompose(n):
    lst = []
    final = []
    sq = n ** 2
    for i in reversed(range(1,n)):
        if sum(lst) == sq:
            final.append(lst)
        else:
            lst.clear()
            lst.append(i ** 2)
        for k in reversed(range(1,i)):
            if sum(lst) + (k ** 2) > sq:
                pass

            else:
                lst.append(k ** 2)

        final.append(lst)
        break
    for j in final:
        if sum(j) == sq:
            j.sort()
            for d in range(len(j)):
                if j.count(j[d]) > 1:
                    return
            for i in range(len(j)):
                j[i] = int(j[i] ** 0.5)
            return j
    return

print()
print()
print(decompose(int(2500**0.5)) == [1,3,5,8,49])
print(decompose(int(7100))==[2,3,5,119,7099])
print(decompose(625)==[2,5,8,34,624])
print(decompose(5)==[3,4])
print(decompose(44)==[2,3,5,7,43])
print(decompose(11)==[1,2,4,10])

