from time import gmtime
actual_year = gmtime()[0]
data = {'Nome': input('Digite seu nome: '),
        'Idade': actual_year - int(input('Ano de nascimento: ')),
        'CTPS': int(input('Carteira de Trabalho (0 = Não tem): '))}
if data['CTPS'] != 0:
    data['Ano de Contratação'] = int(input('Ano de Contratação: '))
    data['Salário'] = float(input(('Salário: R$')))
    data['Aposentadoria'] = (data['Ano de Contratação'] + 35) - (actual_year - data['Idade'])
for k, v in data.items():
    print(f'{k} tem o valor {v}')
