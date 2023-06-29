from random import randint
drawn_numbers = (randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100))
print(f'Os números sorteados foram: {drawn_numbers}')
print(f'O menor valor sorteado foi: {sorted(drawn_numbers)[0]}')
print(f'O maior valor sorteado foi: {sorted(drawn_numbers)[-1]}')

