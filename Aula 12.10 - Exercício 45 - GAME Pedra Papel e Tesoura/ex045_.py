from random import randint
from time import sleep

ia = randint(1, 3)

print()
print('*' * 34)
print(' Vamos jogar Pedra, Papel, Tesoura ')
print()
print(' 1 - Pedra ')
print(' 2 - Tesoura ')
print(' 3 - Papel ')
print('*' * 34)
print()

player = int(input('Digite um valor entre 1 e 3: '))

print()
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('POO...')
sleep(1)
print()

if (player >= 1) and (player <= 3):

    if player == ia:
        print('Você escolheu: {}'.format(player))
        print('O Computador escolheu: {}'.format(ia))
        print()
        print(' * JOGO EMPATADO! * ')
    elif (player == 1 and ia == 2) or (player == 2 and ia == 3) or (player == 3 and ia == 1):
        print('Você escolheu: {}'.format(player))
        print('O Computador escolheu: {}'.format(ia))
        print()
        print(' * PARABENS, VOCÊ VENCEU! * ')
    else:
        print('Você escolheu: {}'.format(player))
        print('O Computador escolheu: {}'.format(ia))
        print()
        print('  * O COMPUTADOR VENCEU! *  ')

else:
    print('Valor digitado: {}'.format(player))
    print('Valor inválido!')
