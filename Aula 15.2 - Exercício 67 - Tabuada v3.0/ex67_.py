v = 1
while v > 0:
    v = int(input('Quer ver a Tabuada de qual valor: '))
    print('-' * 30)

    if v < 0:
        break

    c = 1
    while c <= 10:
        print(f'{v} x {c:2} = {v * c}')
        c += 1
    print('-' * 30)
print('Programa TABUADA encerrado, Volte sempre!')
