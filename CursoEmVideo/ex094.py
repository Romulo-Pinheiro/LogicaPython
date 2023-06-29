people = []
while True:
    personal_data = {'nome': input('Nome: ')}
    gender = input('Sexo [M/F]: ').strip().upper()[0]
    while gender not in ['M', 'F']:
        print('Resposta inválida. Tente novamente!')
        gender = input('Sexo [M/F]: ').strip().upper()[0]
    personal_data['sexo'] = gender
    age = abs(int(input('Idade: ')))
    personal_data['idade'] = age
    people.append(personal_data.copy())
    condition = input('Quer continuar [S/N]? ').strip().upper()[0]
    if condition == 'N':
        break
print('-=' * 30)
print(f'- O grupo tem {len(people)} pessoas.')
sum_age = 0
for data in people:
    sum_age += data['idade']
average_age = sum_age / len(people)
print(f'- A média de idade é de {average_age :.2f}.')
print('- As mulheres cadastradas foram: ', end='')
for data in people:
    if data['sexo'] == 'F':
        print(data['nome'], end=' ')
print('\n- Lista das pessoas com idade acima da média: ')
for data in people:
    if data['idade'] > average_age:
        print(data)
print('<< ENCERRADO >>')
