import PySimpleGUI as sg                        # Part 1 - The import
from Card.Cartas3 import swin, gendeck, pontuação, adicionarcarta, vide


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

class TelaJogo:
    def __init__(self):
        self.pd = gendeck()
        self.cd = gendeck()
        self.pp = pontuação(self.pd)
        self.cp = pontuação(self.cd)
        self.countr = 1
        countl = 0
        countw = 0
        self.layout = [
            [sg.Text(f'Player - {self.pp}',key='pp',size=(25,0)),sg.Text(f'Round {self.countr}')],
            [sg.Text(self.pd, key='pd')],
            [sg.Text(f'CPU - {self.cp}',key='cp')],
            [sg.Text(self.cd,key='cd')]
            ]
        self.row_buttom1 = [[sg.Button("+1",key='+1'),sg.Button("Parar",key='parar'),sg.Button("Sair",key='sair')]]
        self.row_buttom2 = [[sg.Button('Jogar Novamente',key='jn'),sg.Button("Sair",key='sair')]]
        #janela
        self.janela = sg.Window('Blackjack', self.layout + self.row_buttom1)

    def inicar(self):
        # Extração de dados
        while True:
            self.event, self.value = self.janela.read()
            print(self.event,self.value)

            if self.event == 'parar':
                if vide(self.pp,self.cp) == 1:
                    self.janela['pd'].update(f'{"Vitoria":>32}')
                else:
                    self.janela['pd'].update(f'{"DERROTA":>32}')
                self.layout += self.row_buttom2


            if self.event == 'sair' or self.event == sg.WINDOW_CLOSED:
                break

            if self.event == '+1':
                if self.pp <= 21:
                    self.janela['pd'].update(adicionarcarta(self.pd))
                else:
                    self.janela['pd'].update(f'{"DERROTA":>32}')
                    self.janela[0] += self.row_buttom2


            if self.cp <= 16:
                self.janela['cd'].update(adicionarcarta(self.cd))



            self.pp = pontuação(self.pd)
            self.cp = pontuação(self.cd)
            self.janela['pp'].update(f'Player - {self.pp}')
            self.janela['cp'].update(f'CPU - {self.cp}')
            if self.pp >= 22:
                self.janela['pd'].update(f'{"DERROTA":>32}')
                #self.janela['cd'].update(f'{"VITÓRIA":32}')



'''
self.layout.insert(1, [sg.Text(adicionarcarta(self.pd), key='player')])
if self.cp <= 16:
self.layout.insert(1, [sg.Text(adicionarcarta(self.cd), key='player')])
'''

tela = TelaJogo()
tela.inicar()
