n = int(input('\033[1;30mQuer ver a tabuada de qual valor? '))
while n >= 0:
    print('-' * 33)
    for c in range(1, 11):
        print(f'{n} x {c} = {n * c}')
    print('-' * 33)
    n = int(input('Quer ver a tabuada de qual valor? '))
print('-' * 33)
print('PROGRAMA TABUADA ENCERRADO. Volte sempre!')
