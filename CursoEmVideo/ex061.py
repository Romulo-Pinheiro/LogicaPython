n = int(input('Digite um número inteiro para ser o primeiro termo de sua PA: '))
razao = int(input('Digite um número inteiro para ser a razão de sua PA: '))
PA = [n]
while len(PA) < 10:
    PA.append(n)
print(f'Os 10 primeiros termos de sua P.A são:\n{PA}')
