#Gerador de senhas em python

import random, string

tamanho = int(input('Digite o npúero de caracteres'))
chars= string.ascii_letters+string.digits+'!@#$%&*()-=+,.;/?'

rnd=random.SystemRandom() #os.unrandom

print(''.join(rnd.choice(chars)for i in range(tamanho)))
