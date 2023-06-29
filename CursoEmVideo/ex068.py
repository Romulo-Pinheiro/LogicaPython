from random import randint
print('=-'*16)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('=-'*16)
win = 0
while True:
    pc = randint(0, 10)
    jogador = abs(int(input('Diga um valor de 0 a 10: ')))
    while jogador not in range(0, 11):
        print('O número não está entre 0 e 10. Escolha novamente!')
        jogador = abs(int(input('Diga um valor de 0 a 10: ')))
    decisao = str(input('Par ou Ímpar? [P/I] ')).strip().upper()
    while decisao not in ('P', 'I'):
        decisao = str(input('Par ou Ímpar? [P/I] ')).strip().upper()
    par = (pc + jogador) % 2 == 0
    impar = (pc + jogador) % 2 != 0
    if decisao == 'P':
        decisao = par
    elif decisao == 'I':
        decisao = impar
    resultado = 'VENCEU' if decisao is True else 'PERDEU'
    poui = 'PAR' if par is True else 'IMPAR'
    print(f'Você jogou {jogador} e o computador {pc}. Total de {pc + jogador}. DEU {poui}')
    print('-' * 32)
    print(f'Você {resultado}!')
    if decisao is False:
        break
    win += 1
print('=-' * 16)
print(f'GAME OVER. Você venceu {win} vezes.')
