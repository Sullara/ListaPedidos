# Suponha que você esteja criando um aplicativo para anotar os pedidos dos clientes em um restaurante.
# Seu aplicativo precisa de uma lista de pedidos.
# Os garçons adicionam os pedidos a essa lista e os chefes retiram os pedidos da lista.
# Funciona como uma fila.
# Os garçons colocam os pedidos no final da fila e os chefes retiram os pedidos do começo dela para cozinhá-los.


lista_pedidos = []
cod_garçon = 123
cod_chefe = 456
cod_user = 0
pedido = " "

print("Digite -1 para sair")
# Código de identificação o usuário
cod_user=(int(input("Digite o seu cod: ")))

# Loop while que mantém o código rodando pra testar o cod_graçon e cod_chefe na mesma lista
while cod_user != -1:

  # Loop while que permite que o garçon escreva os pedidos
  while cod_user == cod_garçon:
    pedido=(str(input("Digite o pedido:")))

    # Quando digitado "fim" o loop while termina
    if pedido == "fim":
      break
    # Enquanto não chegar ao fim os pedidos continuarão a serem acrescentados a lista
    else:
      lista_pedidos.append(pedido)

  # Novamente solicitando o código de usuário para que seja possível a troca de funções (adicionar e remover itens da lista)
  cod_user=(int(input("Digite o seu cod: ")))

  # Quando o código de identificação do chefe é inserido retorna o último item da lista que também é removido usando o pop
  if cod_user == cod_chefe:
    print(lista_pedidos.pop())