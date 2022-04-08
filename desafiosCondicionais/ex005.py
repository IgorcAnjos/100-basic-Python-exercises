#Questão 5) Faça um programa que leia um ano qualquer e diga se ele é bissexto

ano = int(input('Digite um Ano: '))

if (ano // 1 % 100) % 4 != 0 and (ano // 1 % 1000) != 400:
  print('Esse ano não é bissexto!')
else:
  print('Esse ano é bissexto')
