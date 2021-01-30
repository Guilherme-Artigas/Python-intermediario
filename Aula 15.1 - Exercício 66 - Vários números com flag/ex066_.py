print('*' * 20)
print(' - SOMANDO VALORES - ')
print('*' * 20)

# Temos 2 formas de solucionar esse "problema" ;)

"""c = 1
soma = 0
Qv = 0
while c != 999:
    n = int(input(f'Digite o {c}º valor: '))
    if n == 999:
        break
    c += 1
    soma += n
    Qv += 1
print(f'Resultado da soma entre os valores digitados: {soma}')"""

c = 1
soma = 0
Qv = 0
while c != 999:
    c = int(input('Digite o valor: '))
    if c != 999:
        soma += c
        Qv += 1
print()
print(f'Resultado da soma: {soma}')
print(f'Foram digitados {Qv} valores.')
