#tratamento de erros exceções


#erros personalizados
class Erro(Exception):
    pass

class EntradaErro(Erro):
    def __init__(self,mensagem):
        self.mensagem =mensagem

while True:
    try:
        x=int(input("entre com uma nota de 1 a 10"))
        print(x)
        if x>10:
            raise EntradaErro('Nota não pode ser maior que dez')
        elif x<0:
            raise EntradaErro('Nota não pode ser menor que zero')
        divisao=10/x
        print(divisao)
        break

    except EntradaErro as ex:
        print(ex)
    except ValueError:
        print('Valor inválido')
    except ZeroDivisionError:
        print('não é possível realizar uma divisão por zero')
    except IndexError:
        print('Não encontrado indice')
    except:
        print('Erro desconhecido')
    finally:

        print('final do código')

