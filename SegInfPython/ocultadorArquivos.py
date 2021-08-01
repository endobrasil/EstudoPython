#ocultador de arquivos em pyhton
import ctypes
atributo_ocultar = 0x02

retorno =ctypes.windll.kernel32.SerFileAttributesW('ocultardorArq.txt',atributo_ocultar)

if retorno:
    print("ocultado")
else:
    print("não ocultado")