maior = 0
menor = 0
for c in range(0, 5):
    peso = float(input('Digite seu Peso [KG]: '))

    if (peso > maior):
        maior = peso
    if (menor == 0) or (peso < menor):
        menor = peso

print()

print('Maior peso digitado: {}'.format(maior))
print('Menor peso digitado: {}'.format(menor))
