# Importa a biblioteca random para gerar números aleatórios
import random


class CPFValidator:
    """
    Classe responsável por validar CPFs e gerar CPFs válidos.
    """

    def __init__(self):
        # Método construtor da classe (sem parâmetros adicionais no momento)
        pass

    def validate_cpf(self, cpf):
        """
        Valida um CPF informado.

        Parâmetros:
        - cpf (str): CPF no formato com ou sem pontos e traço.

        Retorna:
        - str: Mensagem informando se o CPF é válido, inválido ou possui valores sequenciais.
        """

        # Remove pontos e traços do CPF informado
        validador_cpf = str(cpf).replace('.', '').replace('-', '')
        verificador = validador_cpf

        # Verifica se todos os dígitos são iguais (sequenciais)
        if validador_cpf == validador_cpf[0] * len(validador_cpf):
            return 'Valores sequenciais!'

        # Calcula o primeiro dígito verificador
        novedigitos_cpf = validador_cpf[:9]
        soma = 0
        contador = 10

        for n in range(9):
            soma += int(novedigitos_cpf[n]) * contador
            contador -= 1

        digito1 = (soma * 10) % 11
        digito1 = digito1 if digito1 <= 9 else 0

        # Adiciona o primeiro dígito ao CPF
        validador_cpf_f = str(novedigitos_cpf) + str(digito1)

        # Calcula o segundo dígito verificador
        soma2 = 0
        contador2 = 11

        for n2 in range(10):
            soma2 += int(validador_cpf_f[n2]) * contador2
            contador2 -= 1

        digito2 = (soma2 * 10) % 11
        digito2 = digito2 if digito2 <= 9 else 0

        # CPF completo gerado para comparação
        validador_cpf_f += str(digito2)

        # Validação final comparando o CPF calculado com o CPF informado
        if validador_cpf_f == verificador:
            return f'O CPF: {verificador[0:3]}.{verificador[3:6]}.{verificador[6:9]}-{verificador[9:11]} é Válido!'
        else:
            return f'O CPF: {verificador[0:3]}.{verificador[3:6]}.{verificador[6:9]}-{verificador[9:11]} é inválido!'

    def generate_cpf(self, quantity):
        """
        Gera uma quantidade de CPFs válidos.

        Parâmetros:
        - quantity (int ou str): Quantidade de CPFs a gerar.

        Retorna:
        - list: Lista com os CPFs gerados e seus respectivos status (sempre 'Válido').
        """

        cpfs = []

        for _ in range(int(quantity)):
            # Gera os 9 primeiros dígitos aleatórios
            base_cpf = ''.join(str(random.randint(0, 9)) for _ in range(9))

            # Calcula o primeiro dígito verificador
            soma = sum(int(base_cpf[i]) * (10 - i) for i in range(9))
            digito1 = (soma * 10) % 11
            digito1 = digito1 if digito1 <= 9 else 0

            # Calcula o segundo dígito verificador
            cpf_parcial = base_cpf + str(digito1)
            soma2 = sum(int(cpf_parcial[i]) * (11 - i) for i in range(10))
            digito2 = (soma2 * 10) % 11
            digito2 = digito2 if digito2 <= 9 else 0

            # CPF completo
            cpf_completo = base_cpf + str(digito1) + str(digito2)

            # Formata no padrão XXX.XXX.XXX-XX
            cpf_formatado = f'{cpf_completo[0:3]}.{cpf_completo[3:6]}.{cpf_completo[6:9]}-{cpf_completo[9:11]}'

            # Adiciona à lista
            cpfs.append([cpf_formatado, 'Válido'])

        return cpfs
