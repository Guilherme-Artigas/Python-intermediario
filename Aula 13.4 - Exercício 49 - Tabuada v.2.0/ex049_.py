n = int(input('Qual o número para consultar a tabuada: '))

for c in range(1, 11):
    print('{:2} x {} = {}'.format(c, n, c * n))
