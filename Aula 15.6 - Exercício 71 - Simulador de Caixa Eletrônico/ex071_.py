from time import sleep

controle = True
nota50 = nota20 = nota10 = nota1 = 0

while controle == True:
    print('=*' * 12)
    print(' ~ BANCO DE ITAPERUÇU ~')
    print('=*' * 12)
    print()
    valor = int(input('Digite o valor para saque: R$ '))

    if valor >= 50:
        nota50 = valor // 50
        valor -= (nota50 * 50)

    if valor >= 20:
        nota20 = valor // 20
        valor -= (nota20 * 20)

    if valor >= 10:
        nota10 = valor // 10
        valor -= (nota10 * 10)

    if valor >= 1:
        nota1 = valor // 1
        valor -= (nota1 * 1)

    controle = False

print()
print(f'Total de {nota50} cédulas de R$ 50')
print(f'Total de {nota20} cédulas de R$ 20')
print(f'Total de {nota10} cédulas de R$ 10')
print(f'Total de {nota1} cédulas de R$ 1')
print('=*' * 12)
print('Volte sempre ao Banco Itaperuçu! Bom dia... ')
sleep(3)
print('OPERAÇÃO FINALIZADA!')
