L1 = float(input('Digite o 1º lado: '))
L2 = float(input('Digite o 2º lado: '))
L3 = float(input('Digite o 3º lado: '))

if L1 < L2 + L3 and L2 < L1 + L3 and L3 < L1 + L2:
    print('Legal Podemos formar um triângulo com os valores digitados!')
    print('... mais esse triângulo é EQUILÁTERO, ESCALENO ou ISÓCELES?')
    print()
    if L1 == L2 and L1 == L3 and L2 == L3:
        print('EQUILÁTERO: todos os lados iguais.')
    elif L1 != L2 and L1 != L3 and L2 != L3:
        print('ESCALENO: todos os lados são diferentes.')
    elif L1 == L2 and L1 != L3 or L1 == L3 and L1 != L2 or L2 == L3 and L2 != L1:
        print('ISÓCELES: dois lados iguais.')
else:
    print('Infelizmente não podemos formar um triângulo com os valores informados!')
