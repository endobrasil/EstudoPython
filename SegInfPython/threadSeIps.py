#exemplos de threads em python
from threading import Thread


def carro(velocidade,piloto):
    trajeto = 0
    while trajeto <=100:
        print('Piloto: {} Km: {}\n'.format(piloto,trajeto))
        trajeto+=velocidade

t_carro1=Thread(target=carro,args=[10,'bruno'])
t_carro2=Thread(target=carro,args=[15,'pytho'])

t_carro1.start()
t_carro2.start()