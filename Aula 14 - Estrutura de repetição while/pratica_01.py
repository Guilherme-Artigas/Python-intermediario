c = -1
qp = 0
qi = 0
while c != 0:
    c = int(input('Digite um valor: '))
    if c != 0:
        if (c % 2 == 0):
            qp += 1
        else:
            qi += 1
print('Quantidade de números pares digitados: {}'.format(qp))
print('Quantidade de números impares digitados: {}'.format(qi))
