from random import randint
from time import sleep
players = {"jogador 1": randint(1, 6), "jogador 2": randint(1, 6),
           "jogador 3": randint(1, 6), "jogador 4": randint(1, 6)}
print('VALORES SORTEADOS:')
for k, v in players.items():
    print(f'\tO {k} tirou {v} ')
    sleep(1)
rank = 1
print('\nRANKING DOS JOGADORES: ')
for i in sorted(players, key=players.get, reverse=True): # Podia ter usado enumerate, já que sorted retorna uma lista
    print(f'\t{rank}° LUGAR: {i} com {players[i]}')
    rank += 1
    sleep(1)
