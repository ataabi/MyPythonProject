from random import choice

def cartas(numer = True):
    numero = choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'Valete', 'Dama', 'Rei'])
    naipe = choice(['Paus', 'Ouros', 'Copas', 'Espadas '])
    return numero, naipe


# player = input('Digite seu nome: ')
playerdeck = []
cpudeck = []

while playerdeck.__len__() != 3:
    try:
        if not carta in playerdeck:
            playerdeck.append(carta)
    except:
        carta = cartas()
    carta = cartas()

while cpudeck.__len__() != 3:
    try:
        if not carta in playerdeck:
            if not carta in cpudeck:
                cpudeck.append(carta)
    except:
        carta = cartas()
    carta = cartas()


playerpoints = 0

for c in playerdeck:
    print(c[0],c)

    if c[0] in (1,2,3,4,5,6,7,8,9,10):
        playerpoints += c[0]

    elif c[0] in 'Valete' 'Dama' 'Rei':
        playerpoints += 10

    elif c[0] == 1:
        if c[0] in 'Valete Dama Rei':
            playerpoints += 11
        else:
            playerpoints += 1

print('\n',playerpoints)

opc2 = 1
if opc2 == 2:
    carta = cartas()
    try:
        if not carta in playerdeck:
            playerdeck.append(carta)
    except:
        carta = cartas()



