
import pickle
import random
def wr():
    a = list(set("""qwe;:,._-/!rtyuiopas df+’ghjklzxcvbnm1
    23456789@0QW£$%&/()=?ERT#€~|YUIO}PA'{SDFGHJ"KXCV*][èéù*Z><^BNM"""))

    '''
    creazione della chiave
    input: prende la prima chiave
    riscrive la chiave in formato dict
    '''
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
    i = a.copy()
    random.shuffle(a)
    j = a.copy()
    random.shuffle(a)
    k = a.copy()
    random.shuffle(a)
    l = a.copy()
    random.shuffle(a)
    m = a.copy()


    df ={}
    df[1] = a
    df[2] = b
    df[3] = c
    df[4] = d
    df[5] = e
    df[6] = f
    df[7] = g
    df[8] = h
    df[9] = i
    df[10] = j
    df[11] = k
    df[12] = l
    df[13] = m




    with open('key.pickle', 'bw') as dh:
        pickle.dump(a, dh)

    with open('crypt.pickle', 'bw') as dg:
        pickle.dump(df, dg)

if __name__ == "__main__":
    wr()

