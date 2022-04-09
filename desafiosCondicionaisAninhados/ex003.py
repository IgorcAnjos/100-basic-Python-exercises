#Questão 3) Escreva um programa que leia dois números inteiros e compare-os mostrando qual é o maior e qual é o menor

n1=int(input('Escreva um número: '))
n2=int(input('Escreva um número: '))

if n1 > n2:
    print(' O maior número é {}, e o menor é {}'.format(n1,n2))
else:
    print('O maior número é {}, e o menor é {}'.format(n2, n1))
