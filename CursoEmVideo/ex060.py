num = abs(int(input('Digite o número que deseja calcular a fatorial: ')))
ant = abs(int(num - 1))
while ant != 0:
    if num == 0:
        num = 1
        break
    num *= ant
    ant -= 1
print(f'A fatorial desse número é: {num}')
