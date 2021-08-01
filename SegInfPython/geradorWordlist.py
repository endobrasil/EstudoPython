#gerador de word list
import itertools
string = input("string a ser permutada:")
resultado=itertools.permutations(string,8)

for i in resultado:
    print(''.join(i))