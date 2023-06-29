matrix = [[], [], []]
sum_even = 0
for index, row in enumerate(matrix):
    for i in range(3):
        value = int(input(f'Digite o valor para [{index}, {i}]: '))
        row.append(value)
print('-=' * 30)
for row in matrix:
    for n in row:
        print(f'[ {n :2}  ]', end='')
        if n % 2 == 0:
            sum_even += n
    print('\n', end='')
print('-=' * 30)
print(f'A soma dos valores pares é {sum_even}.')
print(f'A soma dos valores da terceira coluna é {matrix[0][2] + matrix[1][2] + matrix[2][2]}.')
print(f'O maior valor da 2ª linha é {max(matrix[1])}.')
