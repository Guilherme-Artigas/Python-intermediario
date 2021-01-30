"""
Minha solução...

r = 's'
while r == 's':
    sexo = str(input('Sexo [M/F]: ')).strip().upper()[0]
    if (sexo == 'M'):
        r = 'n'
        print('Dado registrado com sucesso, SEXO: M (Masculino)')
    elif (sexo == 'F'):
        r = 'n'
        print('Dado registrado com sucesso, SEXO: F (Feminino)')
    else:
        print('Você digitou um valor invalido, por favor tente de novo!')
        r = 's'
"""
sexo = str(input('Sexo [M/F]: ')).strip().upper()[0]
while sexo not in 'MmFf':
    print('Dados digitados invalidos, digite novamente!')
    sexo = str(input('Sexo [M/F]: ')).strip().upper()[0]
print('Dados registrados com sucesso. Sexo: {}'.format(sexo))
