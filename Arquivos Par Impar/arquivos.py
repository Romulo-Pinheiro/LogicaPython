numeros = open('numeros.txt', 'w')
for i in range(20):
    valor = int(input('Digite um valor: '))
    numeros.write(f'{valor}\n')
numeros = open('numeros.txt', 'r')
lista_numeros = numeros.read().split('\n')
pares = open('pares.txt', 'w')
impares = open('impares.txt', 'w')
for n in lista_numeros:
    if n != '':
        if int(n) % 2 == 0:
            pares.write(f'{n}\n')
        else:
            impares.write(f'{n}\n')
numeros.close()
pares.close()
impares.close()
