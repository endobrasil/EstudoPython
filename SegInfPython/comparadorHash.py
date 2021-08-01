#comparador de hash em python
import hashlib

arq1='comparadorHasgA.txt'
arq2='comparadorHasgB.txt'

hash1=hashlib.new('ripemd160')
hash1.update(open(arq1, 'rb').read())

hash2 =hashlib.new('ripemd160')
hash1.update(open(arq2, 'rb').read())

if hash1.digest() != hash2.digest():
    print(f'O arquivo: {arq1} é diferente do arquivo {arq2}')
    print(f'O hassh do arquivo {arq1} é {hash1.hexdigest()}'
          f'\nO hassh do arquivo {arq2} é {hash2.hexdigest()}')
else:
    print(f'O arquivo: {arq1} é igual do arquivo {arq2}')


