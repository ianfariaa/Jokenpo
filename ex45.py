from random import randint
from time import sleep
print('Pedra, Papel ou Tesoura:')
itens = ('Pedra', 'Papel', 'Tesoura')
print ('''[ 0 ] PEDRA 
[ 1 ] PAPEL 
[ 2 ] TESOURA ''')
jogador = int(input('Qual é a sua Jogada: '))
computador = randint(0, 2)
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!')
print('-=' * 11)
print('O computador jogou {}'.format(itens[computador]))
print('O jogador jogou {}'.format(itens[jogador]))
print('-=' * 11)
if computador == 0:
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('JOGADOR VENCEU')
    elif jogador == 2:
        print('COMPUTADOR VENCEU')
elif computador == 1:
    if jogador == 0:
        print('COMPUTADOR VENCEU')
    if jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print(' JOGADOR VENCEU')
elif computador == 2:
    if jogador == 0:
        print(' JOGADOR VENCEU')
    elif jogador == 1:
        print(' COMPUTADOR VENCEU')
    elif jogador == 2:
        print('EMPATE')




