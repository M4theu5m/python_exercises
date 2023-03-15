palavra_secreta = 'programa'
tentativas = 0
palavra_aux = ''

print('=-=-=-=-=Jogo de adivinhação=-=-=-=-=')
print('Regras: Adivinhar a palavrar digitando letra por letra')

while True:
  letra_dig = input('\nDigite uma letra: ').lower()
  tentativas += 1

  #Testando possíveis erros do usuário
  if len(letra_dig) == 0:
    print('Nenhuma letra digitada. Tente novamente!')
    continue

  if len(letra_dig) > 1:
    print('Mais de uma letra digitada, digite APENAS uma. Tente novamente!')
    continue

  if letra_dig.isdigit():
    print('Digite apenas letras')
    continue
    
  #Sistema para alocar as letras
  if letra_dig in palavra_secreta:
    palavra_aux += letra_dig
  else:
    print('Letra errada!')

  palavra_nova = ''
  for i in palavra_secreta:
    if i in palavra_aux:
      palavra_nova += i
    else:
      palavra_nova += '*'

  print(palavra_nova)

  #final
  if palavra_secreta == palavra_nova:
    print('\n\nParabéns, você conseguiu!')
    print(f'Palavra secreta: {palavra_nova}')
    print(f'Total de tentativas: {tentativas}')
    break