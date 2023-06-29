matrix = [[], [], []]
for index, row in enumerate(matrix):
    for i in range(3):
        value = int(input(f'Digite o valor para [{index}, {i}]: '))
        row.append(value)
print('-=' * 30)
for row in matrix:
    for n in row:
        print(f'[ {n :2}  ]', end='')
    print()
