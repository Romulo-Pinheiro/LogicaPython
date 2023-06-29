from random import sample
from time import sleep
print('-' * 25)
print(f'{"Jogo da Mega Sena" :^25}')
print('-' * 25)
choices = int(input('Quantos jogos você quer que eu sorteie? '))
print(f'-=-=-= SORTEANDO {choices} JOGOS -=-=-=-')
drawing = [sorted(sample(range(1, 61), k=6)) for i in range(choices)]
for index, numbers in enumerate(drawing):
    print(f'Jogo {index + 1}: {numbers}')
    sleep(1)
print('-=-=-=-= < BOA SORTE ! > -=-=-=-=')
