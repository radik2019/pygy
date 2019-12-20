import datetime

def is_pal(st):
    a = list(st)
    a.reverse()
    return ''.join(a) == st

import time


def palindrom(a):
    nmr = 0
    for i in range(len(a)):
        j = len(a) - i
        for k in range(len(a)):
            pal = a[k:k+j]
            if len(pal)<j:
                break
            time.sleep(0.3)
            print(pal)
            if is_pal(pal):
                
                if len(pal) > nmr:
                    nmr = len(pal)
            if j < nmr:
                return nmr
    return nmr
   
print(palindrom('rarwrara'))




def test_s(function,n):

    t1 = datetime.datetime.now()
    function(n)
    t2 = datetime.datetime.now()
    
    
    return t2 - t1


print(test_s(palindrom,'bd'))
