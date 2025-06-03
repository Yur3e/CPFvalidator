import random

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