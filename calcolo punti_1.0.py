import pickle

while True:
    continua = input('punti "p" o aggiornare la lista "a"\t')
    if continua == 'p':
        op = open('dict.pickle', 'rb')
        prodotto1 = pickle.load(op)
        op.close()

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
                pgr = round(prodotto1[i] * cerc[i], 3)


                so.append(pgr)
            else:
                print(i,' non ce nella lista')
        print()
        print(sum(so), 'punti')
    elif continua == 'lista*':
        op = open('dict.pickle', 'rb')
        prodotto1 = pickle.load(op)
        op.close()
        num = 1
        for i in prodotto1:
            print('{}. {}\t = {}'.format(num, i, prodotto1[i]))
            num += 1
    elif continua == 'a':
        op = open('dict.pickle', 'rb')
        di = pickle.load(op)
        op.close()

        while True:
            nome = input('nome\t')
            if nome == 'stop':
                break
            else:
                peso = int(input('peso\t'))
                punti = int(input('punti\t'))
            di[nome] = punti / peso

        op = open('dict.pickle', 'wb')
        pickle.dump(di, op)
        op.close()
    elif continua == 'cancella':
        op = open('dict.pickle', 'rb')
        di = pickle.load(op)
        op.close()
        formod = input('da canc\t')
        for i in di:
            d = None
            if i == formod:
                d = di.pop(i)
                break
            else:
                pass
        if d == None:
            print('{} non c\'è nella lista'.format(formod))
        op = open('dict.pickle', 'wb')
        pickle.dump(di, op)
        op.close()
    else:
        break

print('alla prossima :)')
