print('=' * 30)
print('10 PRIMEIROS TERMOS DE UMA P.A')
print('=' * 30)

print()

pt = int(input('Primeiro Termo: '))
r = int(input('Razão: '))
decimo = pt + (10 - 1) * r

for c in range(pt, decimo + r, r):
    print(c, end=' > ')
print('acabou!')
