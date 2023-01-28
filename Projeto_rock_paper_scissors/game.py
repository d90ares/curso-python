import os
import random
from sys import platform as pla


def clear_screem():
    if pla == 'linux' or pla == 'linux2' or pla == 'darwin':
        os.system('clear')
    elif pla == 'win32':
        os.system('cls')


move_list = ['pedra', 'papel', 'tesoura']
player_count = 0
cpu_count = 0

def main_print():
    print('='*15)
    print('\nPLACAR:')
    print('Você: {}'.format(player_count))
    print('CPU: {}'.format(cpu_count))
    print('\n')
    print('Escolha uma opção')
    print('0 - PEDRA | 1 - PAPEL | 2 - TESOURA')

def select_move():
    return random.choice(move_list)


def get_player_move():
    while True:
        try:
            player_move = int(input())
            if player_move not in [0, 1, 2]:
                raise
            return move_list[player_move]
        except Exception as e:
            print(e)


def select_winner(p_move, c_move):
    global player_count, cpu_count

    if p_move == 'papel':
        if c_move == 'pedra':
            player_count += 1
            return "p"
        elif c_move == 'tesoura':
            cpu_count += 1
            return 'c'
        else:
            return 'd'

    if p_move == 'pedra':
        if c_move == 'tesoura':
            player_count += 1
            return "p"
        elif c_move == 'papel':
            cpu_count += 1
            return 'c'
        else:
            return 'd'
    
    if p_move == 'tesoura':
        if c_move == 'papel':
            player_count += 1
            return "p"
        elif c_move == 'pedra':
            cpu_count += 1
            return 'c'
        else:
            return 'd'

again = 1
while again == 1:
    main_print()
    player_move = get_player_move()
    cpu_move = select_move()
    winner = select_winner(player_move, cpu_move)

    print('='*15)
    print('SUA JOGADA: {}'.format(player_move.upper()))
    print('JOGADA DA CPU: {}'.format(cpu_move.upper()))

    if winner == 'p':
        print('Você VENCEU!')
    elif winner == 'c':
        print('Você perdeu!')
    else:
        print('EMPATE!')
    print('='*15)

    while True:
        print('Jogar Novamente? 0 - SIM | 1 - NÃO')
        next = int(input())
        if next == 0:
            break
        elif next == 1:
            again == 0
            break
    clear_screem()


