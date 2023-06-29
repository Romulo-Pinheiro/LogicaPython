words = ('aprender', 'programar', 'linguagem',
         'python', 'curso', 'gratis', 'estudar',
         'praticar', 'trabalhar', 'mercado',
         'programador', 'futuro')
for word in words:
    print(f'\nNa palavra {word.upper()} temos ', end='')
    for letter in word.lower():
        if letter in ('a', 'e', 'i', 'o', 'u'):
            print(letter, end=' ')
