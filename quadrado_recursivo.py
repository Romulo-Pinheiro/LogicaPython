def quadrado(n):
    if n == 0 or n == 1:
        return n
    else:
        return quadrado(n - 1) + 2 * (n - 1) + 1


if __name__ == '__main__':
    print(quadrado(2))

