peso = float(input('Digite o seu peso [KG]: '))
altura = float(input('Digite a sua altura: '))

IMC = peso / (altura ** 2)

if IMC < 18.5:
    print('IMC: {:.1f}'.format(IMC))
    print('Abaixo do Peso.')
elif (IMC > 18.5) and (IMC < 25):
    print('IMC: {:.1f}'.format(IMC))
    print('Peso Ideal.')
elif (IMC > 25) and (IMC < 30):
    print('IMC: {:.1f}'.format(IMC))
    print('Esta com Sobrepeso.')
elif (IMC > 30) and (IMC < 40):
    print('IMC: {:.1f}'.format(IMC))
    print('Obesidade.')
else:
    print('IMC: {:.1f}'.format(IMC))
    print('Obesidade Mórbida.')
