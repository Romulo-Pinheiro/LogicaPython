from random import sample
from time import sleep


def sorteia(lista):
    print('Sorteando 5 valores da lista: ', end='')
    lista.extend(sample(range(1, 100), 5))
    for n in lista[-5:]:
        print(n, end=' ')
        sleep(0.25)
    print('PRONTO!')


def somapar(lista):
    soma = 0
    for n in lista:
        if n % 2 == 0:
            soma += n
    print(f'A soma dos pares foi {soma}')


valores = []
sorteia(valores)
print(valores)
somapar(valores)
