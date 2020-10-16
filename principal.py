# EP - Design de Software
# Equipe: Gustavo Oliveira
# Data: 04/10/2020
import random
import defs
 
fichas = 100

jogo1 = defs.jogo()

if jogo1[0] > jogo1[1]:
    print ('Soma 1 ganhou lol')
elif jogo1[0] < jogo1[1]:
    print ('soma 2 ganhou lol')
else:
    print ('empate lol')