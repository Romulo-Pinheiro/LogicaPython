estado = True
x = float(input('\033[1;30mDigite o primeiro valor: '))
y = float(input('Digite o segundo valor: '))
print(f'Os valores que você digitou foram:\n{x} e {y}\n')
while estado:  #Aqui poderia dispensar a variável 'estado' e colocar somente um while True ou while valor != 5
    print('''\033[1;33mQual operação deseja realizar?
    \033[1;30m[ 1 ]\033[1;33m SOMAR
    \033[1;30m[ 2 ]\033[1;33m MULTIPLICAR
    \033[1;30m[ 3 ]\033[1;33m VERIFICAR QUAL O MAIOR
    \033[1;30m[ 4 ]\033[1;33m MUDAR OS NÚMEROS
    \033[1;30m[ 5 ]\033[1;33m SAIR DO PROGRAMA''')
    valor = abs(int(input('\033[1;30mDigite o número da operação desejada:\033[1;33m ')))
    if valor == 1:
        print(f'A soma entre os dois valores é: {x + y}\n')
    elif valor == 2:
        print(f'A multiplicação entre os dois valores é: {x * y}\n')
    elif valor == 3:
        if x > y:
            print(f'O maior valor é: {x}\n')
        elif y > x:
            print(f'O maior valor é: {y}\n')
        else:
            print('Os dois valores são iguais\n')
    elif valor == 4:
        x = float(input('\n\033[1;30mDigite o primeiro valor: '))
        y = float(input('Digite o segundo valor: '))
        print(f'Os valores que você digitou foram:\n{x} e {y}\n')
    elif valor == 5:
        break
    else:
        print('\033[1;31mO valor que você inseriu não é válido. Por favor, insira novamente.\n')
print('\033[1;31m\nPROGRAMA ENCERRADO')
