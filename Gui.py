import PySimpleGUI as sg


class TelaPython:
    def __init__(self):
        # Layout
        layout = [
            [sg.Text('Nome',size=(5,0)),sg.Input(size=(15,0),key='nome')],
            [sg.Text('Idade',size=(5,0)),sg.Input(size=(15,0),key='idade')],
            [sg.Text('Quais provedores de e-mail são aceitos?')],
            [sg.Checkbox('Gmail',key='gmail'),
             sg.Checkbox('Outlook',key='outlook'),
             sg.Checkbox('Yahoo',key='yahoo')],
            [sg.Button('Enviar Dados'),sg.Button('exit',key='exit')],
            [sg.Output(size=(30,10))]
        ]
        # Janela
        self.janela = sg.Window("Dados do usuario").layout(layout)


    def Iniciar(self):
        while True:
            # Extrair os dados da tela
            self.button, self.values = self.janela.Read()
            nome = self.values['nome']
            idade = self.values['idade']
            aceita_gmail = self.values['gmail']
            aceita_outlook = self.values['outlook']
            aceita_yahoo = self.values['yahoo']
            print(f'nome: {nome}\n'
                  f'idade: {idade}\n'
                  f'aceita gmail: {aceita_gmail}\n'
                  f'aceita outlook: {aceita_outlook}\n'
                  f'aceita yahoo: {aceita_yahoo}\n')




tela = TelaPython()
tela.Iniciar()
