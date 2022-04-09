# Questão 1) Escreva um programa para aprovar o emprestimo Bancário de uma casa, ele vai pedir o VALOR DA CASA, O SALÀRIO DO COMPRADOR e em QUANTOS ANOS ELE VAI PAGAR. Calcule o valor da prestação mensal sabendo que ele não pode exceder 30% do salário ou então será negado.

emprestimo = float(input('Valor da casa: R$ '))
salario = float(input('Seu salário: R$ '))
parcelas = int(input("Pretende pagar em quantos anos?"))
n1 = parcelas*12
n2 = salario*0.3

valParcelas = emprestimo/n1

if valParcelas < n2 or valParcelas == n2:
  print('Podemos seguir com seu pedido de emprestimo')
else:
  print("pedido negado!")