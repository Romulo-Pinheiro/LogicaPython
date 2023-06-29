students = []
names = []
while True:
    name = input('Digite o nome do aluno: ')
    names.append(name)
    grade1 = float(input('Nota 1: '))
    grade2 = float(input('Nota 2: '))
    grades = [grade1, grade2]
    names.append(grades[:])
    students.append(names[:])
    names.clear()
    cond = input('Quer continuar [S/N]? ').strip().upper()
    if cond[0] == 'N':
        break
print('-=' * 30)
print(f'{"No." :3} {"NOME" :10} {"MÉDIA" :3}')
print('-' * 21)
for index, student in enumerate(students):
    print(f'{index :<3} {student[0] :10} {sum(student[1])/2 :3.1f}')
print('-' * 21)
while True:
    index = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if index == 999:
        break
    elif 0 <= index < len(students):
        print(f'As notas de {students[index][0]} são {students[index][1]}')
    else:
        print('Posição inválida. Tente novamente')
print('<<< VOLTE SEMPRE >>>')
