import re

#Descobrindo o primeiro dígito
cpf = re.sub(r'[^0-9]', '', '144.339.989-23')#.replace('.', '').replace('-', '')
nove_digitos = cpf[:9]
contador = 10
resultado = 0

for i in nove_digitos:
  resultado += int(i) * contador
  contador -= 1

digito_um = (resultado * 10) % 11
digito_um = digito_um if digito_um <= 9 else 0
print(f'O primeiro digito do final do CPF é: {digito_um}')

#Descobrindo o segundo dígito
dez_digitos = nove_digitos + str(digito_um)
resultado_2 = 0
contador_2 = 10

for x in dez_digitos:
  resultado_2 += int(x) * contador
  contador_2 -= 1

digito_dois = (resultado_2 * 10) % 11
digito_dois = digito_dois if digito_dois <= 9 else 0
print(f'O segundo número final do seu CPF é: {digito_dois}')

#Descobrindo se o CPF é válido ou não
onze_digitos = dez_digitos + str(digito_dois)
print('Cpf válido' if onze_digitos == cpf else 'CPF inválido')
