#maior valor
a=int(input('primeiro valor'))
b=int(input('segundo valor'))
c=int(input('terceiro valor'))

if a>b and a>c:
    m=a
elif b>a and b>c:
    m = b
else:
    m=c


print('O maior valor é {}'.format(m))

#saber se número é par
resto = m%2
if resto==0:
    print('O numero é par')
else:
    print('O numero é impar')

print('final do programa')