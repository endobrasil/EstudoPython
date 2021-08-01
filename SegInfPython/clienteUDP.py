#Cliente UDP com python
import socket

s=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
print("Cliente socket criado com sucesso")

host='localhost'
porta=5432
mensagem="Ola servidor formaza?"

try:
    print("cleinte :"+mensagem)
    s.sendto(mensagem.encode(),(host,porta))
    dados,servidor = s.recvfrom(4086)
    dados=dados.decode()
    print("Cleinte: {}".format(dados))
finally:
    print("fechando a cpnexão")
    s.close()
