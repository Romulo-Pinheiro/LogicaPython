n = abs(int(input('Digite o nº para calcular seu fatorial: ')))
if n == 0 or n == 1:
    print(f'{n}! = ', end='')
    n = 1
else:
    print(f'{n}! = {n} x ', end='')
for i in range(n - 1, 0, -1):
    print(i, end=' x ' if i != 1 else ' = ')
    n *= i
print(f'{n}')
