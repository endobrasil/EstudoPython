#ping em dicversos hosts e diversos IP
import os
import time
with open('pingMultiploHosts.txt') as file:
    dump = file.read()
    #print(dump)
    dump.splitlines() #esta linha deveria ter
                        # colocado as linhas do arquivos
                        #em linhas não funcou

for ip in dump:
    os.system('ping -c 5 {}'.format(ip))
    print('#-'*60)
    time.sleep(5)