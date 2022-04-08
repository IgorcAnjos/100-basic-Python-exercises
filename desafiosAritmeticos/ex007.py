# Questão 7) Crie um programa que leia a altura e a largura de uma parede em metros, calcule sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta 2m².

n8 = float(input('\n A altura da parede : '))
n9 = float(input('\n A largura da parede : '))
area1 = n8*n9
print('\n A área da parede é {}m² e são necessários {}L de tinta para pintá-la inteira'.format(area1, area1/2))
