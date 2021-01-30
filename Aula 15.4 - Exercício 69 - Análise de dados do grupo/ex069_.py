controle = True

mais_dezoito = 0
quantidade_homens = 0
mulheres_menos_de_20 = 0

print('-' * 25)
print(' - CADASTRO DE PESSOAS - ')
print('-' * 25)
print()

while controle == True:

    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MmFf':
        sexo = str(input('Sexo [M/F]: '))

    if idade >= 18:
        mais_dezoito += 1
    if sexo == 'M' or sexo == 'm':
        quantidade_homens += 1
    if sexo == 'F' or sexo == 'f' and idade < 20:
        mulheres_menos_de_20 += 1

    print('-' * 25)
    controle2 = True
    while controle2 == True:
        resposta = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
        if resposta == 'S':
            controle = True
            controle2 = False
        elif resposta == 'N':
            controle = False
            controle2 = False
        elif resposta != 'S' or resposta != 'N':
            print(f'Você digitou uma opção invalida! ... ')
            controle2 = True
    print('-' * 25)

print()
print(f'Menores de 18 anos cadastrados: {mais_dezoito} pessoa(s).')
print(f'Quantidade de homens cadastrados: {quantidade_homens} homen(s).')
print(f'Mulheres menores de 20 anos cadastradas: {mulheres_menos_de_20} mulher(es).')
