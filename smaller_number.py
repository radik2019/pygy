"""
Kata"s name
Next smaller number with the same digits

"""
import itertools
import datetime


def next_smaller(n):
    
    def is_sorted(n):
        lst = list(str(n))[:]
        lst.sort()
        if lst == list(str(n)):
            return True
        return False

    if is_sorted(n):
        return -1

    for k in range(2, len(str(n)) + 1):
        lst = list(itertools.permutations(str(n)[-k:], k))
        lst.sort()
        nm = str(n)[:-k]
        for i in reversed(range(len(lst))):
            if int(nm + ''.join(lst[i])) < n:
                if len(lst[i]) + len(nm) == len(str(n)):
                    return int(nm + ''.join(lst[i]))
    return -1

t = datetime.datetime.now()
print(next_smaller(123456789123456789))


print(1,next_smaller(907) == 790)
print(2,next_smaller(531) == 513)
print(3,next_smaller(135) == -1)
print(4,next_smaller(2071) == 2017)
print(5,next_smaller(414) == 144)
print(6,next_smaller(123456798) == 123456789)
print(7,next_smaller(123456789) == -1)
print(8,next_smaller(1234567908) == 1234567890)

t2 = datetime.datetime.now()
print(t2 - t)


# ___________________________________________

#def next_smaller(n):
#    lst = list(itertools.permutations(str(n),9))
#    lst.sort()
#    for i in reversed(range(len(lst))):
#        if int(''.join(lst[i])) < n:
#            if len(str(n)) < len(lst[i])
#                return lst[i]
#        
#    return -1

