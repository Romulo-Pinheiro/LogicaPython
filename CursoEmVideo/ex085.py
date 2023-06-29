numbers = [[], []]
for i in range(1, 8):
    n = int(input(f'Digite o {i}° valor: '))
    if n % 2 == 0:
        numbers[0].append(n)
    else:
        numbers[1].append(n)
print(f'Os valores pares digitados foram: {sorted(numbers[0])}')
print(f'Os valores ímpares digitados foram: {sorted(numbers[1])}')
