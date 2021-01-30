print('-' * 23)
print(' PROGRESSÃO ARITMETICA ')
print('-' * 23)

p = int(input('Digite o 1º termo: '))
r = int(input('Digite a razão: '))

termo = p
c = 1
l = 11
qt = 0

while c <= l:
    print('{} > '.format(termo), end='')
    termo += r
    c += 1
    qt += 1
    if (c == l):
        print('Pausa')
        l = int(input('Quer prosseguir com mais termos: '))
        if (l >= 1):
            c = 0
        else:
            print('encerra')
print('Progessão finalizada com {} termos mostrados.'.format(qt))
