q = 0
for c in range(1, 8):
    anoN = int(input('Digite o ano de nascicmento da {}º pessoa: '.format(c)))
    idade = 2020 - anoN
    if (idade < 21):
        q += 1
print('Quantidade de pessoas menores de idade:{} pessoas'.format(q))
