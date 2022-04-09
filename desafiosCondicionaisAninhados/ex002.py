# Questão 2) Escreva uma programa que leia um numero inteiro e peça para o usuário escolher qual será a base de conversão, binario, octal e hexadecimal.

num = int(input('Digite um número inteiro: '))
print( '''Escoha uma das bases para conversão:
 [ 1 ] Binario
 [ 2 ] Hexadécimal
 [ 3 ] octal''')
op = int(input('Sua opção: '))

if op > 1:
  if op == 3:
    print('{} convertido para octal fica {}'.format(num, oct(num)[2:]))
  else:
    print('{} convertido para Hexadécimal fica {}'.format(num, hex(num)[2:]))
else:
  print('{} convertido para Binário fica {}'.format(num, bin(num)[2:]))