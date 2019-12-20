

def is_prime(a):
    lst = []
    for i in range(2,a):
        di = a % i
        if di == 0:
            lst.append(i)
    if len(lst) == 0:
        return True
    else:
        return False
def div_prime(a):   
    a = str(a)
    if len(a) >= 3:
        for i in range(1,len(a)):
            left = a[:i]
            right = a[i:]
            if right[0] == '0':
                pass
            else: 
                if is_prime(int(a[i:])) and is_prime(int(a[:i])):
                    return True
                else:
                    pass
    elif len(a) == 2:
        left, right = int(a[0]), int(a[1])
        if is_prime(left) and is_prime(right):
            return True
    else:
        return False
    return False

def rec_prime(n):
    
    if len(n) == 1:
        return is_prime(int(n))
    mid = len(n) // 2
    left = n[:mid]
    right = n[mid:]
    
    gen = rec_prime(left) and rec_prime(right)
    
    return gen



def total_primes(a, b):
    lst = []
    lst2 = []
    for i in range(a,b):
        if is_prime(i):
            lst.append(i)
        else:
            pass
    for k in lst:
        if rec_prime(str(k)):
            lst2.append(k)
        else:
            pass
    print(lst)
    return lst2




print(total_primes(500, 600))
print()
a = [523, 541, 547, 557, 571, 577, 593]
for i in a:
    print(i, rec_prime(str(i)))



