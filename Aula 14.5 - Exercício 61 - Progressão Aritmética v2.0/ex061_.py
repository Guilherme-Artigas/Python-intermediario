print('Gerador de P.A')
print('-*' * 10)
p = int(input('Primeiro termo: '))
r = int(input('Razão: '))
termo = p
c = 1
while c <= 10:
    print('{} > '.format(termo), end='')
    termo += r
    c += 1
print('FIM!')
