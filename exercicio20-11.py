import PySimpleGUI as sg
import random

layout = [
    [sg.Text('Clique no botão para sortear um número de 1 a 100.')],
    # Um Text grande e centralizado para o resultado
    [sg.Text(size=(40, 1), key='-RESULTADO-', justification='center', font=('Helvetica', 20))],
    [sg.Button('Sortear')]
]

window = sg.Window('Sorteador', layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    if event == 'Sortear':
        numero_sorteado = random.randint(1, 100)
        # Atualiza o conteúdo do elemento de texto
        window['-RESULTADO-'].update(f'O número é: {numero_sorteado}')

window.close()