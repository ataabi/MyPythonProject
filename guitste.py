import PySimpleGUI as sg

sg.theme('Dark Blue 3')  # please make your windows colorful

layout =  [[sg.Text(f'{i}. '), sg.In(key=i)] for i in range(1,10)]
layout += [[sg.Button('Save'), sg.Button('Exit')]]

window = sg.Window('Window Title', layout)

while True:  # Event Loop
    event, values = window.read()
    print(event, values)
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    if event == 'Show':
        # change the "output" element to be the value of "input" element
        window['-OUTPUT-'].update(values['-IN-'])

window.close()