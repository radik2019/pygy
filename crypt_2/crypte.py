import random
import pickle
import os
import os.path





def wr():
    '''
    creazione della chiave
    input: prende la prima chiave
    riscrive la chiave in formato dict
    '''
    a = list(set("""qwe;:,._-/!rtyuiopas df+’ghjklzxcvbnm1
        234567890QW£$%&/()=?ERTYUIO}PA'{SDFGHJ"KXCV*][èéù*Z><^BNM"""))

    random.shuffle(a)
    b = a.copy()
    random.shuffle(a)
    c = a.copy()
    random.shuffle(a)
    d = a.copy()
    random.shuffle(a)
    e = a.copy()
    random.shuffle(a)
    f = a.copy()
    random.shuffle(a)
    g = a.copy()
    random.shuffle(a)
    h = a.copy()
    random.shuffle(a)
    j = a.copy()
    random.shuffle(a)
    b1 = a.copy()
    random.shuffle(a)
    c1 = a.copy()
    random.shuffle(a)
    d1 = a.copy()
    random.shuffle(a)
    e1 = a.copy()
    random.shuffle(a)
    f1 = a.copy()
    random.shuffle(a)
    g1 = a.copy()
    random.shuffle(a)
    h1 = a.copy()
    random.shuffle(a)
    j1 = a.copy()


    df ={}
    df[1] = a
    df[2] = b
    df[3] = c
    df[4] = d
    df[5] = e
    df[6] = f
    df[7] = g
    df[8] = h
    df[9] = j
    df[10] = b1
    df[11] = c1
    df[12] = d1
    df[13] = e1
    df[14] = f1
    df[15] = g1
    df[16] = h1
    df[17] = j1

    with open('key.pickle', 'bw') as dh:
        pickle.dump(a, dh)

    with open('crypt.pickle', 'bw') as dg:
        pickle.dump(df, dg)


def ld():
    with open('crypt.pickle', 'rb') as dg:
        d = pickle.load(dg)
    return d


def encode(fras):
    with open('key.pickle', 'rb') as dg:
        alfa = pickle.load(dg)
    df = ld()
    crfr= []
    for i in fras:
        crfr.append(alfa.index(i))
    string = ''
    for i in range(0,len(crfr),17):
        try:
            string += df[1][crfr[i]]
            string += df[2][crfr[i+1]]
            string += df[3][crfr[i+2]]
            string += df[4][crfr[i+3]]
            string += df[5][crfr[i+4]]
            string += df[6][crfr[i+5]]
            string += df[7][crfr[i+6]]
            string += df[8][crfr[i+7]]
            string += df[9][crfr[i+8]]
            string += df[10][crfr[i+9]]
            string += df[11][crfr[i+10]]
            string += df[12][crfr[i+11]]
            string += df[13][crfr[i+12]]
            string += df[14][crfr[i+13]]
            string += df[15][crfr[i+14]]
            string += df[16][crfr[i+15]]
            string += df[17][crfr[i+16]]

        except IndexError:
            pass
        except KeyError:
            pass
    return string


def decode(s):
    with open('key.pickle', 'rb') as dg:
        alfa = pickle.load(dg)
    lst = []
    key = ld()
    
    for i in range(0,len(s),17):
        try:
            lst.append(key[1].index(s[i]))
            lst.append(key[2].index(s[i+1]))
            lst.append(key[3].index(s[i+2]))
            lst.append(key[4].index(s[i+3]))
            lst.append(key[5].index(s[i+4]))
            lst.append(key[6].index(s[i+5]))
            lst.append(key[7].index(s[i+6]))
            lst.append(key[8].index(s[i+7]))
            lst.append(key[9].index(s[i+8]))
            lst.append(key[10].index(s[i+9]))
            lst.append(key[11].index(s[i+10]))
            lst.append(key[12].index(s[i+11]))
            lst.append(key[13].index(s[i+12]))
            lst.append(key[14].index(s[i+13]))
            lst.append(key[15].index(s[i+14]))
            lst.append(key[16].index(s[i+15]))
            lst.append(key[17].index(s[i+16]))


        except IndexError:
            pass
        except KeyError:
            pass
    string = ''
    for i in lst:
        string += alfa[i]
    return string

def encode_file():
    list_file = os.listdir()
    for i in list_file:
        if os.path.isfile(i):
            st = os.path.splitext(i)

            if st[1] == ".txt":
                with open(i, "r") as df:
                    fg = df.read()
                fg = encode(fg)
                with open(i, "w") as df:
                    df.write(fg)
        else:
            pass
    return


def decode_file():
    list_file = os.listdir()
    for i in list_file:
        if os.path.isfile(i):
            st = os.path.splitext(i)

            if st[1] == ".txt":
                with open(i, "r") as df:
                    fg = df.read()
                fg = decode(fg)
                with open(i, "w") as df:
                    df.write(fg)
        else:
            pass
    return



