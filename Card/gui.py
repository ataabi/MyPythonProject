import PySimpleGUI as sg                        # Part 1 - The import
from Card.Cartas3 import swin, gendeck, pontuação, adicionarcarta


'''
# Layout (que tera na tela)
layout = [[sg.Text("Player Name",size=(15,0)),sg.Input(key='nome',size=(10,0))],
        [sg.Button('Ok',key='OK')]]

#janela

janela = sg.Window('Blackajack', layout)
while True:
    eventos, valores = janela.read()
    if eventos == 'OK':
        janela.close()
        break     
'''

playerdeck = gendeck()
cpudeck = gendeck()
countr = 1
countl = 0
countw = 0
while True:
    pp = pontuação(playerdeck)
    cp = pontuação(cpudeck)
    layout2 = [
        [sg.Text(f'Player - {pp}',key='pp',size=(20,0)),sg.Text(f'Round {countr},',size=(20,0)),sg.Text(f'CPU - {cp}')],
        [sg.Text(playerdeck,key='player'),sg.Text(cpudeck)],
        [sg.Button("+1",key='+1'),sg.Button("Parar",key='parar'),sg.Button("Sair",key='sair')]
    ]

    # Janela
    janela2 = sg.Window('Blackjack', layout2)

    eventos2, valores = janela2.read()

    if eventos2 == 'sair' or eventos2 == sg.WINDOW_CLOSED:
        break

    if eventos2 in 'pp' >= 22:
        layout2[1].clear()
        layout2 = [
            [sg.Text(f'Player - {pontuação(playerdeck)}   Round [{countr}]   CPU - {pontuação(cpudeck)}')],
            [sg.Text('DERROTA')],
            [sg.Button("+1", key='+1'), sg.Button("Parar", key='parar'), sg.Button("Sair", key='sair')]
        ]
    if eventos2 == '+1':
        layout2.insert(1,[sg.Text(adicionarcarta(playerdeck),key='player')])
        if cp <=16:
            layout2.insert(1, [sg.Text(adicionarcarta(playerdeck), key='player')])



