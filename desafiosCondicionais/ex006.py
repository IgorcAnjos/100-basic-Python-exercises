# Questão 6) Faça um programa que leia 3 números e diga qual é o maior e qual é o menor.

n1 = float(input('Digite o primeiro número: '))
n2 = float(input('Digite o segundo número: '))
n3 = float(input('Digite o terceiro número: '))

menor = n1
maior = n2

if menor > n2:
  menor = n2
if menor > n3:
  menor = n3
if maior < n1:
  maior = n1
if maior < n3:
  maior = n3

print(' O maior número é: {} \n O menor é: {}'.format(maior, menor))
