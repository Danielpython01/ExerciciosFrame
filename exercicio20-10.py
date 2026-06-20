import PySimpleGUI as sg

# Layout com um texto, um campo de input e dois botões
layout = [
    [sg.Text('Qual é o seu nome?')],
    [sg.Input(key='-NOME-')],
    [sg.Button('OK'), sg.Button('Sair')]
]

# Cria a janela
window = sg.Window('Boas-Vindas', layout)

# Loop de eventos
while True:
    event, values = window.read()
    # Se fechar no 'X' ou clicar em 'Sair'
    if event == sg.WIN_CLOSED or event == 'Sair':
        break
    # Se clicar em 'OK'
    if event == 'OK':
        nome = values['-NOME-']
        # sg.popup é uma forma rápida de mostrar uma mensagem
        sg.popup(f'Olá, {nome}!')

window.close()