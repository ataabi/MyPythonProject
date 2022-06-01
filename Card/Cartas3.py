from random import choice

def cartas():
    numero = choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'Valete', 'Dama', 'Rei'])
    naipe = choice(['Paus', 'Ouros', 'Copas', 'Espadas '])
    return numero, naipe


def gendeck(mincard = 2):
    carta = cartas()
    deck = []
    while len(deck) != mincard:
        try:
            if not carta in deck:
                deck.append(carta)
        except:
            carta = cartas()
        carta = cartas()
    return deck


def pontuação(playerdeck):
    playerpoints = 0
    for c in playerdeck:
        if c[0] in (1, 2, 3, 4, 5, 6, 7, 8, 9, 10):
            playerpoints += c[0]

        elif c[0] in 'Valete' 'Dama' 'Rei':
            playerpoints += 10

        elif c[0] == 1:
            if c[0] in 'Valete Dama Rei':
                playerpoints += 11
            else:
                playerpoints += 1
    return playerpoints


def adicionarcarta(playerdeck,numcard = 1,mincard = 3):
    '''
    :param playerdeck: O Mao do jogador
    :param numcard: O numero de cartas a serem adicionados
    :param mincard: O numero minimo de card na mao
    :return:
    '''
    count = len(playerdeck) + numcard
    carta = cartas()
    if count < mincard:
        playerdeck = gendeck()[:]
    while len(playerdeck) != count:
        if carta in playerdeck:
            carta = cartas()
        else:
            playerdeck.append(carta)

    return playerdeck


def swin(playerdeck):
    if playerdeck[0][0] in [1]:
        if playerdeck[0][0] in [1, 10, "Valete", "Dama", "Rei"]:
            if playerdeck[1][0] in [1, 10, "Valete", "Dama", "Rei"]:
                return 2


def vide(pp, cp):
    '''
    :param pp: Player Points
    :param cp: CPU Points
    :return: 1 = Player Win, 2 = CPU Win
    '''
    if pp == 21 and cp != 21:
        return 1
    if cp == 21 and pp != 21:
        return 0
    if pp >= 22:
        return 0
    if pp <= 21:
        if cp >= 22:
            return 1
        elif pp > cp:
            return 1
        elif cp > pp:
            return 0
