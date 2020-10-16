import random

def pegar_carta(baralho:list)->list:
    naipe = random.randint(0, 3)
    valor = random.randint(0, len(baralho[naipe])-1)
    numero = recebeString(baralho[naipe][valor])
    # a = str(baralho[naipe][valor])
    # index_valor = baralho_limpo.index(a)
    # numero = baralho[4][index_valor]
    return [numero, naipe, valor]

#recebendo string e transformando em valores
def recebeString(s:str)->int:
    baralho_limpo = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    valores = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 0, 0, 0]
    index = baralho_limpo.index(s)
    return valores[index]
    #tem que devolver o valor da carta
    #ex. recebe a string Q e devolve 0
    #if se a carta for 10, j, Q, K return 0
    #elif a return 1
    #int carta para o resto.

def jogo()->list:
    soma1 = 0
    soma2 = 0
    baralho = [['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K'], ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K'], ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K'], ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K'], [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 0, 0, 0]]

    cartinha1 = pegar_carta(baralho)
    carta = baralho[cartinha1[1]][cartinha1[2]]
    baralho[cartinha1[1]].pop(cartinha1[2])
    soma1 = soma1 + recebeString(carta)

    cartinha2 = pegar_carta(baralho)
    carta = baralho[cartinha2[1]][cartinha2[2]]
    baralho[cartinha1[1]].pop(cartinha1[2])
    soma1 = soma1 + recebeString(carta)

    cartinha3 = pegar_carta(baralho)
    carta = baralho[cartinha3[1]][cartinha3[2]]
    baralho[cartinha1[1]].pop(cartinha1[2])
    soma2 = soma2 + recebeString(carta)

    cartinha4 = pegar_carta(baralho)
    carta = baralho[cartinha4[1]][cartinha4[2]]
    baralho[cartinha1[1]].pop(cartinha1[2])
    soma2 = soma2 + recebeString(carta)
    if soma1 < 5:
        carta_extra = pegar_carta(baralho)
        carta = baralho[carta_extra[1]][carta_extra[2]]
        baralho[cartinha1[1]].pop(cartinha1[2])
        soma1 = soma1 + carta_extra[0]
    if soma2 < 5:
        carta_extra = pegar_carta(baralho)
        carta = baralho[carta_extra[1]][carta_extra[2]]
        baralho[cartinha1[1]].pop(cartinha1[2])
        soma2 = soma2 + carta_extra[0]
    return [soma1, soma2]