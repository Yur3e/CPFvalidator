import random
import sys
import PySimpleGUI as sg

class CPFValidator:
    def __init__(self):
        pass
    
    def validate_cpf(self, cpf):
        validador_cpf = str(cpf).replace('.', '').replace('-', '')
        verificador = validador_cpf
        multin = validador_cpf[0] * len(validador_cpf)
        
        if validador_cpf == multin:
            return 'Valores sequenciais!'

        novedigitos_cpf = validador_cpf[:9]
        some = 0
        contador = 10
        
        for n in range(9):
            some += (int(novedigitos_cpf[n]) * contador)
            contador -= 1
            digito1 = ((some * 10) % 11)
            digito1 = digito1 if digito1 <= 9 else 0

        validador_cpf_f = str(novedigitos_cpf) + str(digito1)

        some2 = 0
        contador2 = 11
        
        for n2 in range(10):
            some2 += (int(validador_cpf_f[n2]) * contador2)
            contador2 -= 1
            
        digito2 = ((some2 * 10) % 11)
        digito2 = digito2 if digito2 <= 9 else 0 

        validador_cpf_f += str(digito2)

        if validador_cpf_f == verificador:
            return f'O CPF: {verificador[0]}{verificador[1]}{verificador[2]}.{verificador[3]}{verificador[4]}{verificador[5]}.{verificador[6]}{verificador[7]}{verificador[8]}-{verificador[9]}{verificador[10]} é Válido!'
        else:
            return f'O CPF: {verificador[0]}{verificador[1]}{verificador[2]}.{verificador[3]}{verificador[4]}{verificador[5]}.{verificador[6]}{verificador[7]}{verificador[8]}-{verificador[9]}{verificador[10]} é inválido!'

    def generate_cpf(self, quantity):
        cpfs = []

        for _ in range(int(quantity)):
            validador_cpf = ''
            
            for i in range(9):
                validador_cpf += str(random.randint(0, 9))

            some = 0
            contador = 10
            
            for n in validador_cpf:
                some += (int(n) * contador)
                contador -= 1
                
            digito1 = ((some * 10) % 11)
            digito1 = digito1 if digito1 <= 9 else 0

            validador_cpf_f = str(validador_cpf) + str(digito1)
            some2 = 0
            contador2 = 11
            
            for n2 in validador_cpf_f:
                some2 += (int(n2) * contador2)
                contador2 -= 1
                
            digito2 = ((some2 * 10) % 11)
            digito2 = digito2 if digito2 <= 9 else 0 
            validador_cpf_f += str(digito2)
            
            verificador = str(validador_cpf) + str(digito1) + str(digito2)
            
            if validador_cpf_f == verificador:
                cpfs.append([f'{verificador[0]}{verificador[1]}{verificador[2]}.{verificador[3]}{verificador[4]}{verificador[5]}.{verificador[6]}{verificador[7]}{verificador[8]}-{verificador[9]}{verificador[10]}', 'Válido'])
            else: 
                cpfs.append([f'{verificador[0]}{verificador[1]}{verificador[2]}.{verificador[3]}{verificador[4]}{verificador[5]}.{verificador[6]}{verificador[7]}{verificador[8]}-{verificador[9]}{verificador[10]}', 'Inválido'])
        
        return cpfs

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
        expand_x=True,  # Expand horizontally
        expand_y=True,  # Expand vertically
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
