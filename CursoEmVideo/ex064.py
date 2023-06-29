soma = 0
qnt = 0
while True:
    n = int(input('\033[1;30mDigite um número inteiro (Digite 999 para encerrar): '))
    if n == 999:
        break
    soma += n
    qnt += 1
print(f'\033[1;30m{qnt} números foram digitados\nA soma dos números digitados é: {soma}')
