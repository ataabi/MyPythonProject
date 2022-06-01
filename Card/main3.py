from Card.Cartas3 import swin, gendeck, pontuação, adicionarcarta


print('\033[33m  ♠♣♥♦  Blackjack.  ♠♣♥♦  (v1.0)\033[m')
playerdeck = gendeck()
cpudeck = gendeck()
countr = 1 #Contador do round
countw = 0 #contador de vitoria
countl = 0 #contador de derrota

while True:
    print(f'Round [\033[34m{countr}\033[m]:')
    print(f'Cartas do jogador.')
    for c in playerdeck:
            print(f'\033[30:44m{c}\033[m',end= ' ')

    print(f'\nCartas do Computador')
    for c in cpudeck:
            print(f'\033[30:41m{c}\033[m',end= ' ')
    print(f'\n    \033[32mPontuação\033[m   ')
    print(f'[JOGADOR]    \033[35m{pontuação(playerdeck)}\033[m')
    print(f'[COMPUTADOR] \033[35m{pontuação(cpudeck)}\033[m')

    if swin(playerdeck) == 2:
        countl += 1
        print('Você VENCEU')
        print('Jogar Novamente ?')
        print('[1]SIM [2]NÃO')
        opc = int(input(': '))
        if opc == 1:
            playerdeck = gendeck()
            cpudeck = gendeck()
            countr += 1
        elif opc == 2:
            break
    elif swin(cpudeck) == 2:
        print('Você PERDEU')
        print('Jogar Novamente ?')
        print('[1]SIM [2]NÃO')
        opc = int(input(': '))
        if opc == 1:
            playerdeck = gendeck()
            cpudeck = gendeck()
            countr += 1
        elif opc == 2:
            break

    elif pontuação(playerdeck) > 21:
        print('Você PERDEU')
        print('Jogar Novamente ?')
        print('[1]SIM [2]NÃO')
        opc = int(input(': '))
        if opc == 1:
            playerdeck = gendeck()
            cpudeck = gendeck()
            countr += 1
        elif opc == 2:
            break

    elif pontuação(cpudeck) > 21:
        countl += 1
        print('Você VENCEU')
        print('Jogar Novamente ?')
        print('[1]SIM [2]NÃO')
        opc = int(input(': '))
        if opc == 1:
            playerdeck = gendeck()
            cpudeck = gendeck()
            countr += 1
        elif opc == 2:
            break

    elif pontuação(playerdeck) < 21:
        print('[1]+1 Carta ? [2] PARAR')
        opc = int(input(': '))
        if opc == 1:
            playerdeck = adicionarcarta(playerdeck)
            if pontuação(cpudeck) <= 16:
                cpudeck = adicionarcarta(cpudeck)

        elif opc == 2:
            while pontuação(cpudeck) <= 16:
                adicionarcarta(cpudeck)
            print(f'Cartas do jogador.')
            for c in playerdeck:
                print(f'\033[30:44m{c}\033[m', end=' ')

            print(f'\nCartas do Computador')
            for c in cpudeck:
                print(f'\033[30:41m{c}\033[m', end=' ')
            print(f'\n    \033[32mPontuação\033[m   ')
            print(f'[JOGADOR]    \033[35m{pontuação(playerdeck)}\033[m')
            print(f'[COMPUTADOR] \033[35m{pontuação(cpudeck)}\033[m')
            if pontuação(playerdeck) > pontuação(cpudeck):
                print('Você VENCEU')
                countw += 1
                print('Jogar Novamente ?')
                print('[1]SIM [2]NÃO')
                opc = int(input(': '))
                if opc == 1:
                    playerdeck = gendeck()
                    cpudeck = gendeck()
                    countr += 1
                elif opc == 2:
                    break

            elif pontuação(cpudeck) > pontuação(playerdeck):
                if pontuação(cpudeck) >= 22 and pontuação(playerdeck) <=21:
                    countw += 1
                    print('Voce venceu')
                    print('[1]SIM [2]NÃO')
                    opc = int(input(': '))
                    if opc == 1:
                        playerdeck = gendeck()
                        cpudeck = gendeck()
                        countr += 1
                    elif opc == 2:
                        break
                else:
                    print('Você PERDEU')
                    countl += 1
                    print('Jogar Novamente ?')
                    print('[1]SIM [2]NÃO')
                    opc = int(input(': '))
                    if opc == 1:
                        playerdeck = gendeck()
                        cpudeck = gendeck()
                        countr += 1
                    elif opc == 2:
                        break

    elif pontuação(playerdeck) == 21:
        countw += 1
        print('Voce venceu')
        print('[1]SIM [2]NÃO')
        opc = int(input(': '))
        if opc == 1:
            playerdeck = gendeck()
            cpudeck = gendeck()
            countr += 1
        elif opc == 2:
            break

    elif pontuação(cpudeck) == 21:
        countl += 1
        print('Voce PERDEU')
        print('[1]SIM [2]NÃO')
        opc = int(input(': '))
        if opc == 1:
            playerdeck = gendeck()
            cpudeck = gendeck()
            countr += 1
        elif opc == 2:
            break


    print('-'*70)

print(f' Você Jogou {countr}\n Ganhou {countw}\n Perdeu {countl}')
print('Obrigado por jogar.')
