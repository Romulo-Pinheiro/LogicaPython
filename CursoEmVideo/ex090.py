student_data = {}
name = input('Nome do aluno: ')
student_data["Nome"] = name
average_grade = float(input(f'Média de {name}: '))
student_data["Média"] = average_grade
if average_grade >= 7:
    student_data["Situação"] = "Aprovado"
else:
    student_data["Situação"] = "Reprovado"
print('-=' * 30)
for k, v in student_data.items():
    print(f'{k} é igual a {v}')
