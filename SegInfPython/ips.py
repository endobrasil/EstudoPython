#trabalhado com ips
import ipaddress
ip='192.168.0.1'
ip_red='192.168.0.0/24'

endereco = ipaddress.ip_address(ip)
rede = ipaddress.ip_network(ip_red)
print(endereco+1000)
print(rede)

for ipe in rede:
    print(ipe)

