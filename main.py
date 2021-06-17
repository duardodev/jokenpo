from random import randint
from time import sleep
import os

os.system('cls')

print('\033[32m=\033[m' * 40)
print('J O K E N P Ô '.center(40))
print('\033[32m=\033[m' * 40)

input('Pressione ENTER para começar o jogo...')
os.system('cls')

while True:
    jogador = int(input(
        '--------------------------\n'
        '|     OPÇÕES DO JOGO     |\n'
        '--------------------------\n'
        '|    [ 1 ]  -  PEDRA     |\n'
        '|    [ 2 ]  -  PAPEL     |\n'
        '|    [ 3 ]  -  TESOURA   |\n'
        '--------------------------\n'
        'Digite uma opção: '))

    computador = randint(1, 3)
    lista = [1, 2, 3]
    os.system('cls')

    while jogador not in lista:
        jogador = int(input(
        '--------------------------\n'
        '|     OPÇÕES DO JOGO     |\n'
        '--------------------------\n'
        '|    [ 1 ]  -  PEDRA     |\n'
        '|    [ 2 ]  -  PAPEL     |\n'
        '|    [ 3 ]  -  TESOURA   |\n'
        '--------------------------\n'
        'Opção invalida! Digite novamente uma opção: '))
        os.system('cls')

    print('\033[34mJO...\033[m')
    sleep(1)
    print('\033[34mKEN...\033[m')
    sleep(1)
    print('\033[34mPÔ!\033[m')
    sleep(0.5)
    os.system('cls')

    if jogador == 1 and computador == 1:
        print('\033[33m----------- EMPATOU -----------\033[m')
        print('Você escolheu PEDRA ✊\nComputador escolheu PEDRA ✊')
        print('\033[33m-------------------------------\033[m')
    elif jogador == 2 and computador == 2:
        print('\033[33m----------- EMPATOU -----------\033[m')
        print('Você escolheu PAPEL 🖐️\nComputador escolheu PAPEL 🖐️')
        print('\033[33m-------------------------------\033[m')
    elif jogador == 3 and computador == 3:
        print('\033[33m----------- EMPATOU -----------\033[m')
        print('Vocêe escolheu TESOURA ✌️\nComputador escolheu TESOURA ✌️')
        print('\033[33m-------------------------------\033[m')


    if jogador == 1 and computador == 3:
        print('\033[32m---------- VOCÊ VENCEU ----------\033[m')
        print('Você escolheu PEDRA ✊\nComputador escolheu TESOURA ✌️')
        print('\033[32m---------------------------------\033[m')
    elif jogador == 2 and computador == 1:
        print('\033[32m---------- VOCÊ VENCEU ----------\033[m')
        print('Você escolheu PAPEL 🖐️\nComputador escolheu PEDRA ✊')
        print('\033[32m---------------------------------\033[m')
    elif jogador == 3 and computador == 2:
        print('\033[32m---------- VOCÊ VENCEU ----------\033[m')
        print('Você escolheu TESOURA ✌️\nComputador escolheu PAPEL 🖐️')
        print('\033[32m---------------------------------\033[m')
            

    if computador == 2 and jogador == 1:
        print('\033[31m---------- VOCÊ PERDEU ----------\033[m')
        print('Computador escolheu PAPEL 🖐️\nVocê escolheu PEDRA ✊')
        print('\033[31m---------------------------------\033[m')
    elif computador == 3 and jogador == 2:
        print('\033[31m---------- VOCÊ PERDEU ----------\033[m')
        print('Computador escolheu TESOURA ✌️\nVocê escolheu PAPEL 🖐️')
        print('\033[31m---------------------------------\033[m')
    elif computador == 1 and jogador == 3:  
        print('\033[31m---------- VOCÊ PERDEU ----------\033[m')
        print('Computador escolheu PEDRA ✊\nVocê escolheu TESOURA ✌️')
        print('\033[31m---------------------------------\033[m')


    jogar_novamente = str(input('Você quer jogar novamente? [s/n]: ')).lower()[0]

    while jogar_novamente not in 'sn':
        jogar_novamente = str(input('Você quer jogar novamente? [s/n]: ')).lower()[0]

    if jogar_novamente == 'n':
        print('\033[31mEncerrando o jogo...\033[m')
        sleep(2)
        os.system('cls')

        print('\033[32m=\033[m' * 40)
        print('Jogo encerrado. Obrigado por jogar!'.center(40))
        print('\033[32m=\033[m' * 40)
        break