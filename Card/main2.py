from Card.Cartas3 import cartas, gendeck, pontuação, adicionarcarta


print('\033[33mVamos jogar Blackjack.(Alpha version.)\033[m')
playerdeck = gendeck()
cpudeck = gendeck()
countr = 1 #Contador do round
countw = 0 #contador de vitoria
countl = 0 #contador de derrota

while True:
    print(f'Round [{countr}]:')
    print(f'Cartos do jogador.'
          f'   \033[30:41m{playerdeck}\033[m')
    print((f'Cartas do Computador'
           f' \033[30:41m{cpudeck}\033[m'))
    print(f'    Pontos   \n[JOGADOR]    \033[m{pontuação(playerdeck)}\033[m '
          f'')
    print(f'[COMPUTADOR] \033[m{pontuação(cpudeck)}\033[m')

    if pontuação(playerdeck) > 21:
        countl += 1
        print('Você PERDEU')
        print('Jogar Novamente ?')
        print('[1]SIM [2]NÃO')
        opc = int(input(': '))
        if opc == 1:
            playerdeck.clear()
            playerdeck = gendeck()
            cpudeck.clear()
            cpudeck = gendeck()
        elif opc == 2:
            break

    elif pontuação(cpudeck) > 21:
        countl += 1
        print('Você VENCEU')
        print('Jogar Novamente ?')
        print('[1]SIM [2]NÃO')
        opc = int(input(': '))
        if opc == 1:
            playerdeck.clear()
            playerdeck = gendeck()
            cpudeck.clear()
            cpudeck = gendeck()
        elif opc == 2:
            break

    elif pontuação(playerdeck) < 21:
        print('[1]+1 Carta ? [2] PARAR')
        opc = int(input(': '))
        if opc == 1:
            playerdeck = adicionarcarta(playerdeck)
            cpudeck = adicionarcarta(cpudeck)
        elif opc == 2:
            if pontuação(playerdeck) > pontuação(cpudeck):
                print('Você VENCEU')
                countw += 1
                print('Jogar Novamente ?')
                print('[1]SIM [2]NÃO')
                opc = int(input(': '))
                if opc == 1:
                    playerdeck.clear()
                    playerdeck = gendeck()
                    cpudeck.clear()
                    cpudeck = gendeck()
                elif opc == 2:
                    break

            elif pontuação(cpudeck) > pontuação(playerdeck):
                print('Você PERDEU')
                countl += 1
                print('Jogar Novamente ?')
                print('[1]SIM [2]NÃO')
                opc = int(input(': '))
                if opc == 1:
                    playerdeck.clear()
                    playerdeck = gendeck()
                    cpudeck.clear()
                    cpudeck = gendeck()
                elif opc == 2:
                    break

    elif pontuação(playerdeck) == 21:
        countw += 1
        print('Voce venceu')
        print('[1]SIM [2]NÃO')
        opc = int(input(': '))
        if opc == 1:
            playerdeck.clear()
            playerdeck = gendeck()
            cpudeck.clear()
            cpudeck = gendeck()
        elif opc == 2:
            break

    elif pontuação(cpudeck) == 21:
        countl += 1
        print('Voce PERDEU')
        print('[1]SIM [2]NÃO')
        opc = int(input(': '))
        if opc == 1:
            playerdeck.clear()
            playerdeck = gendeck()
            cpudeck.clear()
            cpudeck = gendeck()
        elif opc == 2:
            break

    countr += 1
    print('-'*70)

print(f' Você Jogou {countr}\n Ganhou {countw}\n Perdeu {countl}')
print('Obrigado por jogar.')
