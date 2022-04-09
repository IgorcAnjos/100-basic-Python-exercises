# Questão 4) Crie um programa que gerencie o aproveitamento de um jopgador de futebol. O programa vai ler o nome e quantas partidas ele jogou depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será guardado em um dicionáro incluindo o total de gols feitos durante o campeonato.

AproveitamentoJogador = dict()
s = 0

print('=== Campeonato Brasileiro de Fotebolas!! ===')

AproveitamentoJogador['nome'] = str(input('Escreva o nome: '))
AproveitamentoJogador['Partidas jogadas'] = int(input('Quantidade de partidas jogadas: '))

for c in range(0, AproveitamentoJogador['Partidas jogadas']):
  AproveitamentoJogador[f'Gols feitos na {c+1}° partida: '] = int(input(f'Quantidade de gols feitos na {c+1}° partida'))
  s += AproveitamentoJogador[f'Gols feitos na {c+1}° partida: ']
AproveitamentoJogador['Total de gols'] = s

print('*****Analise de jogador*****')

for k, v in AproveitamentoJogador.items():
    print(f'- {k}: {v}')
