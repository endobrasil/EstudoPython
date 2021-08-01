#verificador de telefones

import phonenumbers
from phonenumbers import geocoder


fone=input('Digite o etlefone no formato: +558532362085: ')

fone_numero=phonenumbers.parse(fone)

print(geocoder.description_for_number(fone_numero, 'pt'))