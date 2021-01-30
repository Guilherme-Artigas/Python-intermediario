r = 's'
maior = menor = soma = media = q = 0

while r == 's':
    n = int(input('Digite um valor: '))
    q += 1
    soma += n

    if (n > maior):
        maior = n
    if (menor == 0) or (n < menor):
        menor = n

    r = str(input('Quer continuar? [S/N]: ')).lower()

media = soma / q
print()
print('Média: {}'.format(media))
print('Maior valor digitado {}'.format(maior))
print('Menor valor digitado {}'.format(menor))

