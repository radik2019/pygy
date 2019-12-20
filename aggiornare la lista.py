
import pickle
op = open('dict.pickle', 'rb')
di = pickle.load(op)
op.close()

print(di)

while True:
    nome = input('nome\t')
    if nome == 'stop':
        break
    else:
        peso = int(input('peso\t'))
        punti = int(input('punti\t'))
    di[nome] = punti / peso

op = open('dict.pickle','wb')

pickle.dump(di, op)
op.close()