from random import randint

a = randint(0, 10)

q = 0
c = 0
while c != a:
    c = int(input('Digite um valor: '))
    q += 1
    if (c > a):
        print('Menos, tente outra vez!')
    else:
        print('Mais, tente de novo!')

print()
print('Parabens! voce acertou!')
print('Foram {} tentativas'.format(q))
print('Numero sorteado pelo computador foi {}.'.format(a))
