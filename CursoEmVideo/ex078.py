numbers = []
for i in range(5):
    n = int(input(f'Digite um valor para a posição {i}: '))
    numbers.append(n)
print(f'Você digitou os valores {numbers}')
print('-=' * 25)
print(f'O maior valor digitado foi {max(numbers)}. Nas posições: ', end='')
for position, n in enumerate(numbers):
    if n == max(numbers):
        print(f'{position}... ', end='')
print(f'\nO menor valor digitado foi {min(numbers)}. Nas posições: ', end='')
for position, n in enumerate(numbers):
    if n == min(numbers):
        print(f'{position}... ', end='')
