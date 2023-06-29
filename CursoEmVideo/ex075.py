n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
n3 = int(input('Digite mais um número: '))
n4 = int(input('Digite um último número: '))
written_numbers = (n1, n2, n3, n4)
print(f'Você digitou os números {written_numbers}')
print(f'O número 9 apareceu {written_numbers.count(9)} vez(es)')
if 3 in written_numbers:
    print(f'A primeira posição em que o valor 3 aparece é {written_numbers.index(3) + 1}ª')
else:
    print('O valor 3 não foi digitado')
print(f'Os valores pares digitados foram: ', end='')
for n in written_numbers:
    if n % 2 == 0:
        print(n, end=' ')
