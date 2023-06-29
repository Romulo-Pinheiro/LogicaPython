n = int(input('Digite um número inteiro para ser o primeiro termo de sua PA: '))
razao = int(input('Digite um número inteiro para ser a razão de sua PA: '))
PA = [n]
while len(PA) < 10:
    n += razao
    PA.append(n)
print(f'\033[1;33mOs 10 primeiros termos de sua P.A são:\n{PA}\033[m')
total = 10
termos = abs(int(input('Quantos termos a mais você deseja mostrar? Digite 0 se deseja encerrar o programa: ')))
while termos != 0:
    PA.clear()
    while len(PA) < termos:
        n += razao
        PA.append(n)
    print(f'\033[1;33mOs próximos {termos} termos dessa P.A são:\n{PA}\033[m')
    total += termos
    termos = abs(int(input('Quantos termos a mais você deseja mostrar? Digite 0 se deseja encerrar o programa: ')))
print('\033[1;31mFim')
print(f'Total de termos = {total}')