import PySimpleGUI as sg
from classes.gerador import CPFValidator

cpf_validator = CPFValidator()

layout = [
    [sg.Text('Digite qual opção você deseja:')],
    [sg.Radio('Verificar CPF existente', 'OPTIONS', key='-VERIFY-')],
    [sg.Radio('Gerar CPFS válidos', 'OPTIONS', key='-GENERATE-')],
    [sg.Text('CPF:'), sg.Input(key='-CPF-')],
    [sg.Text('Quantidade:'), sg.Input(key='-QUANTITY-')],
    [sg.Button('Executar'), sg.Button('Sair')],
    [sg.Table(
        values=[],
        headings=['CPF', 'Status'],
        key='-TABLE-',
        enable_events=True,
        justification='center',
        num_rows=10,
        col_widths=[15, 10],
        auto_size_columns=True,
        expand_x=True,  
        expand_y=True,  
    )],
]

window = sg.Window('Validador de CPF', layout)

while True:
    event, values = window.read()

    if event == sg.WINDOW_CLOSED or event == 'Sair':
        break
    elif event == 'Executar':
        if values['-VERIFY-']:
            cpf = values['-CPF-']
            result = cpf_validator.validate_cpf(cpf)
            window['-TABLE-'].update(values=[[cpf, result]])
        elif values['-GENERATE-']:
            quantity = values['-QUANTITY-']
            results = cpf_validator.generate_cpf(quantity)
            window['-TABLE-'].update(values=results)

window.close()