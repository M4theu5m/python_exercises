#Lista de compras

import os
lista_compras = []

while True:
  try:
    tentativa = input('\nSelecione uma opção:\n1 - Inserir\n2 - Apagar\n3 - Listar\n4 - Encerrar Programa\n-> ')
    opcao = int(tentativa)
  except:
    print('\nEssa opção não existe!')
    continue

  os.system('cls')

  #Adicionando produtos na lista
  if opcao == 1:
    os.system('cls')
    print('Digite o Produto:')
    produto = input('-> ')
    lista_compras.append(produto)

  #Removendo produtos da lista
  elif opcao == 2:
    os.system('cls')
    try:
      valor = int(input('Digite a posição que você deseja apagar: '))
      del lista_compras[valor]
    except:
      print('\nNão foi possível apagar, esse número não existe na lista')
      continue

  #Mostrando a lista
  elif opcao == 3:
    os.system('cls')
    if len(lista_compras) == 0:
      print('Não existe produtos para listar')
      continue
    for indice, item in enumerate(lista_compras):
      print (indice, item)

  #Encerrando o programa
  elif opcao == 4:
    os.system('cls')
    print('Obrigado por utilizar nosso serviço')
    break

  else:
    print('Essa opção não existe')