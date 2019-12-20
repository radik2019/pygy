

import hashlib



def crypt(s):
    n = hashlib.sha256(bytes(s, 'utf-8'))
    n_hash = n.hexdigest()
    return n_hash


sha = 'f62a17341e3875c73b72994c574c58fe7d30a644cd6f81e295d9cb3c9202304d'


inh = input('nome   ')
if crypt(inh) == sha:
	print('giusto')
else:
	print('errato')

