# EP - Design de Software
# Equipe: Gustavo Oliveira
# Data: 04/10/2020
import random
import math
import defs

fichas1 = 100
fichas2 = 100
fichas3 = 100
fichas4 = 100

continua = input('Gostariam de Jogar? digite sim ou não: ')
jogar = continua == 'sim'

while(jogar == True):
    jogo1 = defs.jogo()
    pergunta1 = input('Jogador 1, adivinhe quem vai ganhar: Mesa (M), Jogador (J) ou Empate (E): ')
    aposta1 = int(input('quantas fichas gostaria de apostar? você tem {} fichas: '.format(fichas1)))
    pergunta2 = input('Jogador 2, adivinhe quem vai ganhar: Mesa (M), Jogador (J) ou Empate (E): ')
    aposta2 = int(input('quantas fichas gostaria de apostar? você tem {} fichas: '.format(fichas2)))
    pergunta3 = input('Jogador 3, adivinhe quem vai ganhar: Mesa (M), Jogador (J) ou Empate (E): ')
    aposta3 = int(input('quantas fichas gostaria de apostar? você tem {} fichas: '.format(fichas3)))
    pergunta4 = input('Jogador 4, adivinhe quem vai ganhar: Mesa (M), Jogador (J) ou Empate (E): ')
    aposta4 = int(input('quantas fichas gostaria de apostar? você tem {} fichas: '.format(fichas4)))
    jogador1 = defs.jogador(pergunta1, jogo1, aposta1, fichas1)
    print(jogador1[0])
    fichas1 = jogador1[1]
    print('jogador 1 tem: ' + str(fichas1))

    jogador2 = defs.jogador(pergunta2, jogo1, aposta2, fichas2)
    fichas2 = jogador2[1]
    print('jogador 2 tem: ' + str(fichas2))

    jogador3 = defs.jogador(pergunta3, jogo1, aposta3, fichas3)
    fichas3 = jogador3[1]
    print('jogador 3 tem: ' + str(fichas3))

    jogador4 = defs.jogador(pergunta4, jogo1, aposta4, fichas4)
    fichas4 = jogador4[1]
    print('jogador 4 tem: ' + str(fichas4))

    continua = input('gostaria de continuar? digite sim ou não: ')
    jogar = continua == 'sim'
    if min([fichas1, fichas2, fichas3, fichas4]) <= 0:
        print('Algum jogador não tem fichas. Jogo encerrará.')
        continua = False