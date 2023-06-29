def write(text):
    length = len(text) + 4
    print('~' * length)
    print(f'{text :^{length}}')
    print('~' * length)


write('Olá, mundo')
write('CeV')
write('Curso de Python no Youtube')