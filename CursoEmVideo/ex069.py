maior18 = homem = mulher20 = n = 0
while True:
    print('-' * 30)
    n += 1
    print(f'{n}ª Pessoa')
    idade = abs(int(input('Idade: ')))
    sexo = str(input('Sexo [M/F]: ')).strip().upper()
    while sexo not in ['M', 'F']:
        print('Resposta inválida. Leia com atenção e escreva novamente.')
        sexo = str(input('Sexo [M/F]: ')).strip().upper()
    if idade > 18:
        maior18 += 1
    if sexo == 'M':
        homem += 1
    if sexo == 'F' and idade < 20:
        mulher20 += 1
    continua = str(input('Quer continuar [S/N]? ')).strip().upper()
    while continua not in ['S', 'N']:
        print('Resposta inválida. Leia com atenção e escreva normalmente.')
        continua = str(input('Quer continuar [S/N]? ')).strip().upper()
    if continua == 'N':
        break
print(f'\nDas pessoas cadastradas:\n{maior18} tem mais de 18 anos.')
print(f'{homem} são homens.')
print(f'{mulher20} são mulheres com menos de 20 anos.')
