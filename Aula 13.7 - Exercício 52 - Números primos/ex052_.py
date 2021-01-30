n = int(input('Digite um número: '))

total = 0

for c in range(1, n + 1):
    if n % c == 0:
        print('\033[34m', end=' ')
        total += 1
    else:
        print('\033[m', end=' ')
    print('{}'.format(c), end=' ')

print('\n\033[mO número {} foi divisivel {} vezes.'.format(n, total))
if total == 2:
    print('{} é um número primo!'.format(n))
else:
    print('{} não é um número primo.'.format(n))
