import random
import pickle

alfa = list('qwertyuiopas dfghjklzxcvbnm1234567890QWERTYUIOPASDFGHJKLZXCVBNM')
#random.shuffle(a)
#b = a.copy()


#random.shuffle(a)

#c = a.copy()
#random.shuffle(a)
#d = a.copy()
#random.shuffle(a)
#e = a.copy()
#random.shuffle(a)

#df ={}
#df[1]=a
#df[2]=b
#df[3] = c
#df[4] = d
#df[5] = e
#alfa = list('qwertyuiopas dfghjklzxcvbnm')
#def wr():
#    with open('crypt.pickle', 'bw') as dg:
#        pickle.dump(df,dg)

#wr()
def ld():
    with open('crypt.pickle', 'rb') as dg:
        d = pickle.load(dg)
    return d

df = ld()
crfr= []
fras = input('frase:  ')

for i in fras:
    crfr.append(alfa.index(i))


str = ''
for i in range(0,len(crfr),5):
    
    try:
        str += df[1][crfr[i]]
        str += df[2][crfr[i+1]]
        str += df[3][crfr[i+2]]
        str += df[4][crfr[i+3]]
        str += df[5][crfr[i+4]]
    except IndexError:
        pass
print(str)


def decod(s):
    lst = []
    key = ld()
    
    for i in range(0,len(s),5):
        try:
        
            lst.append(key[1].index(s[i]))
            lst.append(key[2].index(s[i+1]))
            lst.append(key[3].index(s[i+2]))
            lst.append(key[4].index(s[i+3]))
            lst.append(key[5].index(s[i+4]))
        except IndexError:
            pass
    print(lst)

decod('ciao')