numbers = []
for i in range(5):
    n = int(input('Digite um valor: '))
    if not numbers or n >= numbers[-1]:
        numbers.append(n)
        print('Valor adicionado ao final da lista')
    elif n <= numbers[0]:
        numbers.insert(0, n)
        print('Valor adicionado na posição 0 da lista')
    else:
        pointer = 1
        for elem in numbers[1:]:
            if n <= elem:
                numbers.insert(pointer, n)
                print(f'Valor adicionado na posição {pointer}')
                break
            pointer += 1
print(f'Os valores digitados em ordem crescente: {numbers}')
    