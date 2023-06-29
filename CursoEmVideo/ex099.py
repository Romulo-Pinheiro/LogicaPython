from time import sleep


def maior(*numeros):
    print('-='*30)
    print('Analisando os valores passados...')
    maior_valor = 0
    for i, n in enumerate(numeros):
        if i == 0 or n > maior_valor:
            maior_valor = n
        print(n, end=' ')
        sleep(0.25)
    print(f'\nForam informados {len(numeros)} valores ao todo')
    print(f'O maior valor informado foi {maior_valor}')


maior(19, 21, 12, 40, 35)
maior(850, 210, 850, 3, 17)
maior(3, 7, 5)
maior(4)
maior()
