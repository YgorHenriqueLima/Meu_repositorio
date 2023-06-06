# trabalhando com número de telefone
# referencia: https://pypi.org/project/phonenumbers/
# ajuste do telefone para usarmos o phonenumber
import phonenumbers
telefone = "+5581985492977"
telefone_ajustado = phonenumbers.parse(telefone, "BR")
print(telefone_ajustado)

# descobrir localização do telefone
from phonenumbers import geocoder
local = geocoder.description_for_number(telefone_ajustado, 'pt-br')
print(local)

telefone_formulário =  "+5581985492977"
telefone_formulário_ajustado = phonenumbers.parse(telefone_formulário, "BR")
telefone_formatado = phonenumbers.format_number(telefone_formulário_ajustado,
                                                phonenumbers.PhoneNumberFormat.NATIONAL)
print(telefone_formatado)

# descobrir a operadora do telefone
from phonenumbers import carrier
operadora = carrier.name_for_number(telefone_ajustado, "pt-br")
print(operadora)

# retirar um telefone de um texto
corpo_email = """
prezados,

Quando tiverem uma resposta da proposta, favor entrar em contato

abs,
Ygor
(81)98549-2977)

"""
for telefone in phonenumbers.PhoneNumberMatcher(corpo_email, "BR"):
    print(telefone)