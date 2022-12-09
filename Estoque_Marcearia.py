listaProdutos = []

def cadastrarProduto(cod): #função 1 - cadastramento de produto
  print('Bem-vindo ao cadastrar Produto')
  input('Digite o código do produto: ')
  nome = input('Digite o nome do produto: ')
  fabricante = input('Digite o fabricante do produto: ')
  valor = int(input('Digite o valor do produto em reais: '))
  dicionarioProduto = {'cod'        : cod,
                       'nome'       : nome,
                       'fabricante' : fabricante,
                       'valor'      : valor}
  listaProdutos.append(dicionarioProduto.copy())


def consultarProduto(): #função 2 - consultar produto
  print('Bem-vindo ao consultar produtos')
  while True:
    try:
      opConsulta = int(input('Entre com a opção desejada:\n'
                             '1 - Consultar todos os produtos:\n'
                             '2 - Consultar produtos por código:\n'
                             '3 - Consultar produtos por fabricantes:\n'
                             '4 - Retornar\n'
                             '>> '))
      if opConsulta == 1:
        print('Consulta de produtos')
        for produto in listaProdutos:
          for key, value in produto.items():
            print('{} : {}'.format(key, value))
      elif opConsulta == 2:
        print('Consulta de códigos:')
        entrada = int(input('Digite o código: '))
        for produto in listaProdutos:
          if (produto['cod']) == entrada:
            for key, value in produto.items():
              print('{} : {}'.format(key, value))
      elif opConsulta == 3:
        print('Consulta de fabricantes: ')
        entrada = (input('Consulta de fabricante do produto: '))
        for produto in listaProdutos:
          if (produto['fabricante']) == entrada:
            for key, value in produto.items():
              print('{} : {}'.format(key, value))
      elif opConsulta == 4:
        return #também pode usar break
      else:
        print('Números inválidos') #erro de digitação
        continue
    except ValueError:
      print('Operação inválida') #erro de digitação


def removerProduto(): #Função 3 - remover produto
  print('Remoção de produto:')
  entrada = int(input('Digite o código desejado: '))
  for produto in listaProdutos:
    if(produto['cod'] == entrada):
      listaProdutos.remove(produto)


#Início programa
print('Bem-vindo ao controle de estoque da Mercearia do Elias Lorandi')
estoque = 0
while True:
  try:
    opcao = int(input('Digite a opção desejada: \n'
                      '1 - Cadastrar produto: \n'
                      '2 - Consultar produto: \n'
                      '3 - Remover produto: \n'
                      '4 - Sair\n'
                      '>> '))
    if opcao == 1:
      estoque = estoque + 1
      cadastrarProduto(estoque)
    elif opcao == 2:
      consultarProduto()
    elif opcao == 3:
      removerProduto()
    elif opcao == 4:
      print('Programa encerrado')
      break
    else:
      print('Número inválido')
      continue
  except ValueError:
    print('Valor inválido')