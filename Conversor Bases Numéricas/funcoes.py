def decimal(numero, base):
    lista = []
    expoente = len(numero)
    letras = {'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}
    for i in numero.upper():
        if i in letras.keys():
            i = letras[i]
        expoente -= 1
        if int(i) > 0:
            digito = int(i) * base ** expoente
            lista.append(digito)
    return sum(lista)


def conversor(numero, base_conversao):
    quociente = numero
    lista = []
    hexad = {10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}
    while quociente >= base_conversao:
        resto = quociente % base_conversao
        quociente = quociente // base_conversao
        lista.append(resto)
    lista.append(quociente)
    lista.reverse()
    for indice, elemento in enumerate(lista):
        if elemento > 9:
            lista[indice] = hexad[elemento]
    return ''.join(str(elemento) for elemento in lista)
