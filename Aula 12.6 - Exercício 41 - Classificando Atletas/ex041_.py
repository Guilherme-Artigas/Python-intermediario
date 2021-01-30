anoN = int(input('Digite o ano de nascimento: '))

print()

print(' - 9 Anos: Mirim ')
print(' - 14 Anos: Infantil ')
print(' - 19 Anos: junior ')
print(' - 20 Anos: Sênior ')
print(' - Acima dos 20 Anos: Master ')

print()

idade = 2020 - anoN

if idade < 10:
    print('O candidato tem {} anos, portanto esta na categoria Mirim.'.format(idade))
elif idade < 15:
    print('O candidato tem {} anos, portanto esta na categoria Infantil.'.format(idade))
elif idade < 20:
    print('O candidato tem {} anos, portanto esta na categoria Junior.'.format(idade))
elif idade < 21:
    print('O candidato tem {} anos, portanto esta na categoria Sênior.'.format(idade))
else:
    print('O candidato tem {} anos, portanto esta na categoria Master.'.format(idade))
