#trabalhando com datas
from datetime import date, time, datetime

def trabalhando_com_date():
    data_atual = date.today()
    print(data_atual)
    print(data_atual.strftime('%A %B %Y'))

def trabalhando_com_time():
    horario = time(hour=15, minute=18, second=30)
    print(horario)
    horario_str=horario.strftime('%H:%M:%S')
    print(horario_str)

def trabalhando_com_datetime():
    data_atual = datetime.now()
    print(data_atual)
    print(data_atual.strftime('%H:%M:%S'))
    print(data_atual.strftime('%c'))
    tupla=('segunda','terça','quarta','quinta','sexta','sabado','domingo')
    print(tupla[data_atual.weekday()])

if __name__ == '__main__':
    trabalhando_com_date()
    trabalhando_com_time()
    trabalhando_com_datetime()