n1 = float(input('Digite a 1º nota: '))
n2 = float(input('Digite a 2º nota: '))

media = (n1 + n2) / 2

if media < 4.9:
    print('Média: {}'.format(media))
    print('REPROVADO!')
elif (media > 5.0) and (media < 6.9):
    print('Média: {}'.format(media))
    print('RECUPERAÇÃO!')
else:
    print('Média: {}'.format(media))
    print('APROVADO!')
