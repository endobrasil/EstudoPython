#um ping com python
import os #recursus do S.O.

ip_ou_host=input("digite o ip o host")
print("#"*60)
os.system('ping -c 100 {}'.format(ip_ou_host))
print("#"*60)