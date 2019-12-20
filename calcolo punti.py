import pickle

op = open('dict.pickle', 'rb')
prodotto1 = pickle.load(op)
op.close()


while True:
    continua = input('continuare? "si" o "no"\t')
    if continua == 'si':

        def s(prodotto, peso):
            if prodotto  in prodotto1:
                print(prodotto1[prodotto] * peso)
            else:
                print('non ce')
        key = 'asdkhfgksdhf'
        cerc = {}
        while True:
            key = input('prodotto\t')
            if key == 'stop':
                break
            else:
                peso = int(input('peso\t\t'))

                cerc[key] = peso
        print(cerc)
        so = []
        for i in cerc:
            if i in prodotto1:
                somma = (prodotto1[i] * cerc[i])

                so.append(somma)
            else:
                print(i,' non ce nella lista')
        print()
        print(sum(so), 'punti')
    else:
        break