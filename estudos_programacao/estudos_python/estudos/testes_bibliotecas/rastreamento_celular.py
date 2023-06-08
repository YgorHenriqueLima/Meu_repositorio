# phonenumbers funções
import phonenumbers
from phonenumbers import geocoder
from phonenumbers import carrier
import googlemaps
from geopy.geocoders import Nominatim # função para encontrar o endereço do dispositivo

def lin():
    print('-='*30)


lin()
print('digite um numero seu')
lin()

# informação da localização em tempo real onde a pessoa se encontra e a operadora
numero = str(input('digite o numero do celular: '))
ch_numero = phonenumbers.parse(numero, 'CH')
lin()
print('local:', geocoder.description_for_number(ch_numero, 'en'))
lin()
operadora = phonenumbers.parse(numero, 'RO')
print('Operadora:', carrier.name_for_number(operadora, "en")