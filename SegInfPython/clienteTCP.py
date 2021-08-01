#Cliente TCP em python
import socket
import sys

def main():
    try:
        s=socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)

    except socket.error as e:
        print('conexão falhou')
        print('Erro {}'.format(e))
        sys.exit()

    print("socket criado com sucesso!!!")

    HostAlvo=input("digite o Ip a ser conectado")
    PortaAlvo=input("digite a porta a ser conectada")

    try:
        s.connect((HostAlvo, int(PortaAlvo)))
        print("Cliente TCP conectado com sucesso no host: {}"
              "e na porta: {}".format(HostAlvo,PortaAlvo))
        s.shutdown(2)

    except socket.error as e:
        print("Não foi possível conectar no host: {} na porta: {}".format(HostAlvo, PortaAlvo))
        print("Erro: {}".format(e))
        sys.exit()

if __name__ == "__main__":
    main()


