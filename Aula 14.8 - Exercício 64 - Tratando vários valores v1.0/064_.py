c = 0
qnd = 0
soma = 0

while c != 999:
    c = int(input('Digite um valor: '))
    if (c != 999):
        soma += c
        qnd += 1

print()

print('Soma = {}'.format(soma))
print('Quantidade de números lidos pelo teclado: {} números'.format(qnd))
