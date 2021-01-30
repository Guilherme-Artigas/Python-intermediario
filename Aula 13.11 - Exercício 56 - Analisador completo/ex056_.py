soma = 0
midade = 0
qm = 0
for c in range(1, 5):
    print(' ---------- {}º Pessoa ---------- '.format(c))
    nome = str(input('Digite o nome: '))
    idade = int(input('Digite a idade: '))
    sexo = str(input('Digite o sexo [M/F]: '))

    soma += idade

    if (sexo == 'M') or (sexo == 'm') and (idade > midade):
        h = nome
    if (sexo == 'F') or (sexo == 'f') and (idade < 20):
        qm += 1

media = soma / 4
print()

print(' ** Resultado **')
print('Média de idade do grupo de pessoas {} anos.'.format(media))
print('Nome do homem mais velho: {}'.format(h))
print('Quantidade de mulheres menores de 20 anos {} mulheres'.format(qm))
