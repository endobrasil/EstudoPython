#variáveis

a = int(input('Entre primeiro valor'))
b = int(input('entre segunda valor'))

soma = a+b
subtracao = a-b
multiplicacao=a*b
divisao = a/b
resto = a%b

print('Soma: {som}. '
      '\nSubtracao {sub}'
      '\nDivisao {div}'
      '\nMultiplicacao {mul}'
      '\nResto {res}'.format(som=soma,
                             sub=subtracao,
                             div=divisao,
                             mul=multiplicacao,
                             res=resto))

