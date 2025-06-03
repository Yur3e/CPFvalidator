# Importa a biblioteca PySimpleGUI para criar a interface gráfica
import PySimpleGUI as sg

# Importa a classe CPFValidator que contém métodos para validação e geração de CPF
from classes.gerador import CPFValidator

# Cria uma instância do validador de CPF
cpf_validator = CPFValidator()

# Define o layout da janela
layout = [
    [sg.Text('Digite qual opção você deseja:')],
    [sg.Radio('Verificar CPF existente', 'OPTIONS', key='-VERIFY-')],
    [sg.Radio('Gerar CPFS válidos', 'OPTIONS', key='-GENERATE-')],
    [sg.Text('CPF:'), sg.Input(key='-CPF-')],
    [sg.Text('Quantidade:'), sg.Input(key='-QUANTITY-')],
    [sg.Button('Executar'), sg.Button('Sair')],
    [sg.Table(
        values=[],  # Tabela começa vazia
        headings=['CPF', 'Status'],  # Cabeçalhos da tabela
        key='-TABLE-',  # Chave para referenciar a tabela no código
        enable_events=True,
        justification='center',  # Centraliza o texto
        num_rows=10,  # Número de linhas visíveis na tabela
        col_widths=[15, 10],  # Largura das colunas
        auto_size_columns=True,
        expand_x=True,  
        expand_y=True,  
    )],
]

# Cria a janela principal
window = sg.Window('Validador de CPF', layout)

# Loop principal da aplicação
while True:
    event, values = window.read()

    # Se clicar no botão "Sair" ou fechar a janela, encerra o programa
    if event == sg.WINDOW_CLOSED or event == 'Sair':
        break

    # Quando clica em "Executar"
    elif event == 'Executar':
        # Se selecionou a opção de verificar CPF
        if values['-VERIFY-']:
            cpf = values['-CPF-']
            result = cpf_validator.validate_cpf(cpf)  # Valida o CPF inserido
            window['-TABLE-'].update(values=[[cpf, result]])  # Atualiza a tabela com o resultado

        # Se selecionou a opção de gerar CPFs válidos
        elif values['-GENERATE-']:
            quantity = values['-QUANTITY-']
            results = cpf_validator.generate_cpf(quantity)  # Gera os CPFs válidos
            window['-TABLE-'].update(values=results)  # Atualiza a tabela com os CPFs gerados

# Fecha a janela quando sai do loop
window.close()
