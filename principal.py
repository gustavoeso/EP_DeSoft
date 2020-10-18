# EP - Design de Software
# Equipe: Gustavo Oliveira
# Data: 04/10/2020
import random
import math
import defs

jogo1 = defs.jogo()

fichas = 100

continua = input('Gostaria de Jogar? digite sim ou não: ')
jogar = continua == 'sim'

while(jogar == True):
    pergunta = input('Adivinhe quem vai ganhar: Mesa (M), Jogador (J) ou Empate (E): ')
    aposta = int(input('quantas fichas gostaria de apostar? você tem {} fichas: '.format(fichas)))
    if aposta < fichas:
        if (pergunta == 'M'):
            if (jogo1[0] > jogo1[1]):
                print ('Ganhou a Mesa')
                fichas += math.floor((aposta)*0.95)
                comissão = (aposta * 1.06) - aposta
                fichas -= comissão
            else:
                print('Perdeu')
                fichas -= math.floor((aposta)*0.95)
        elif (pergunta == 'J'):
            if(jogo1[0] < jogo1[1]):
                print ('Ganhou o Jogador')
                fichas += aposta
                comissão = (aposta * 1.24) - aposta
                fichas -= comissão
            else:
                print('Perdeu')
                fichas -= aposta
        elif (pergunta =='E'):
            if (jogo1[0] == jogo1[1]):
                print ('Ganhou o Empate')
                fichas += aposta * 8
                comissão = (aposta * 14.36) - aposta
                fichas -= comissão
            else:
                print('Perdeu')
                fichas -= aposta * 8
    else:
        print('Você não tem fichas o suficiente')
    
    print('Suas fichas atuais: {}'.format(fichas))
    continua = input('gostaria de continuar? digite sim ou não: ')
    jogar = continua == 'sim'
    if fichas <= 0:
        print('Você não tem fichas.')
        continua = False