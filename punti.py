import pickle

# prodotto1 = {
#         'agnello cosciotto':3 /60,
#         'manzo filetto':3 / 120,
#         'prosciutto di parma':1 / 20,
#         'mortadella':2 / 20,
#         'pesce':0.03, 'uova':0.01,
#         'gnocchi di patate': 0.04, 'pasta cotta': 0.03,
#         'pasta cruda': 0.1,
#         'riso bianco cotto': 0.03333333333333333,
#         'riso bianco crudo': 0.1, 'riso integrale cotto': 0.04,
#         'riso integrale crudo': 0.1, 'cornflakes': 0.1,
#         'couscous cotto': 0.03333333333333333,
#         'couscous crudo': 0.1, 'farro': 0.1,
#         'bresaola': 0.03333333333333333,
#         'prosciutto cotto': 0.03333333333333333,
#         'salame': 0.1,
#         'olio':1 / 5
#                  }
#
# op = open('dict.pickle','wb')
#
# pickle.dump(prodotto1, op)
# op.close()


op = open('dict.pickle', 'rb')
prodotto1 = pickle.load(op)
op.close()
print(prodotto1)
