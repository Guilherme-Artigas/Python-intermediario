somaP = 0
for c in range(1, 6):
    n = int(input('Digite um valor: '))
    if (n % 2 == 0):
        somaP += n
print('Soma dos valores pares digitados = {}'.format(somaP))
