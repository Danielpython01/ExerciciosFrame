import PySimpleGUI as sg

sg.theme('GreenTan')

# Tenta carregar tarefas de um arquivo para persistência
try:
    with open('tarefas.txt', 'r') as f:
        # .strip() remove espaços em branco e quebras de linha
        tarefas = [linha.strip() for linha in f.readlines()]
except FileNotFoundError:
    tarefas = [] # Se o arquivo não existe, começa com uma lista vazia

# sg.Column permite agrupar elementos verticalmente
coluna_esquerda = [
    [sg.Text('Minhas Tarefas:')],
    # enable_events=True faz com que clicar em um item da lista gere um evento
    [sg.Listbox(values=tarefas, size=(40, 10), key='-LISTA-', enable_events=True)],
    [sg.Button('Remover Tarefa Selecionada')]
]

coluna_direita = [
    [sg.Text('Nova Tarefa:')],
    [sg.Input(key='-NOVA_TAREFA-', size=(30,1))],
    [sg.Button('Adicionar')]
]

# sg.VSeperator() cria uma linha vertical separadora
layout = [
    [sg.Column(coluna_esquerda), sg.VSeperator(), sg.Column(coluna_direita)]
]

window = sg.Window('Lista de Tarefas', layout)

# Função auxiliar para salvar a lista no arquivo
def salvar_tarefas(lista_tarefas):
    with open('tarefas.txt', 'w') as f:
        for tarefa in lista_tarefas:
            f.write(tarefa + '\n')

while True:
    event, values = window.read()
    
    if event == sg.WIN_CLOSED:
        break

    if event == 'Adicionar':
        nova_tarefa = values['-NOVA_TAREFA-']
        if nova_tarefa: # Garante que não está adicionando uma tarefa vazia
            tarefas.append(nova_tarefa)
            window['-LISTA-'].update(values=tarefas) # Atualiza a lista na tela
            window['-NOVA_TAREFA-'].update('') # Limpa o campo de input
            salvar_tarefas(tarefas)

    if event == 'Remover Tarefa Selecionada':
        # O valor de um Listbox é uma lista de itens selecionados
        tarefas_selecionadas = values['-LISTA-']
        if tarefas_selecionadas:
            tarefa_para_remover = tarefas_selecionadas[0]
            tarefas.remove(tarefa_para_remover)
            window['-LISTA-'].update(values=tarefas)
            salvar_tarefas(tarefas)

window.close()