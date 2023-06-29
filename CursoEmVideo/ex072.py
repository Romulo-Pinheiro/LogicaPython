infull_numbers = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito',
                  'nove', 'dez', 'onze', 'doze', 'treze', 'catorze', 'quinze', 'dezesseis',
                  'dezessete', 'dezoito', 'dezenove', 'vinte')
num = int(input('Digite um número entre 0 e 20: '))
while not (0 <= num <= 20):
    num = int(input('Tente novamente. Digite um número entre 0 e 20: '))
print(f'Você digitou o número {infull_numbers[num]}.')
