

def is_pal(st):
    a = list(st)
    a.reverse()
    return ''.join(a) == st



a = 'arrirrvedercii'
nmr = 0
for i in range(len(a)):
    for k in range(len(a)):
        if is_pal(a[k:k+i]):
            print(a[k:k+i])
            nmr = len(a[k:k+i])
            break
   
print(nmr)

