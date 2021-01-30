from random import randint

controle = True

q = 0
while controle == True:
    print('=-' * 16)
    print(' =- VAMOS JOGAR PAR OU ÍMPAR -= ')
    print('=-' * 16)

    v = int(input('Digite um valor entre [1 e 10]: '))
    j = ' '
    while j not in 'PpIi':
        j = str(input('Par ou Ímpar? [P/I]: ')).strip().upper()[0]
    ia = randint(1, 10)

    s = v + ia

    if j == 'P' and s % 2 == 0 or j == 'I' and s % 2 != 0:
        print('-' * 60)
        print(f'Você jogou {v} e o computador jogou {ia}. Total de {s}! deu ', end='')
        if s % 2 == 0:
            print('Par')
        else:
            print('Ímpar')
        q += 1
        print('-' * 60)
        print('Você Venceu!')
        print('Vamos jogar novamente!')
        print()
    else:
        print('-' * 60)
        print(f'Você jogou {v} e o computador jogou {ia}. Total de {s}! deu ', end='')
        if s % 2 == 0:
            print('Par')
        else:
            print('Ímpar')
        print('-' * 60)
        print('Você Perdeu!')
        controle = False

    print('=-' * 16)

print(f'GAME OVER! Você venceu {q} vezes.')
