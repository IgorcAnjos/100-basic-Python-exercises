#Questão 9) Elabore um programa que calcule o valor a ser pago por um produto considerando o seu preço normal e condição de pagamento: A vista dinheiro ou cheque 10% de desconto, A vista no cartão: 5% de desconto, Em até duas vezes no cartão, preço normal, 3x ou mais no cartão com 20% de juros.

pre = float(input('Qual é o valor desse produto?'))
print(''' Escolha sua forma de pagamento!
[ 1 ] A vista ou em Cheque.
[ 2 ] A vista no cartão.
[ 3 ] Até 2x no cartão.
[ 4 ] x3 ou Mais no cartão.''')
op = int(input('Digite Aqui: '))

if op == 4:
  print('Sua compra ficará em {}'.format(pre + pre*0.2))
elif op == 3:
  print('Sua compra ficará em {}'.format(pre))
elif op == 2:
  print('Sua compra ficará em {}'.format(pre - pre*0.05))
elif op == 1:
  print('Sua compra ficará em {}'.format(pre - pre*0.1))
