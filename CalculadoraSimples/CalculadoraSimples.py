
estado_calculadora = {
    'valor_atual': 0,
    'expressao_atual': '',
    'ultimo_valor': None,
    'ultima_operacao': None,
}

def limpar_ultimo_valor():
    estado_calculadora['valor_atual'] = estado_calculadora['ultimo_valor']
    estado_calculadora['ultimo_valor'] = None
    print(estado_calculadora['expressao_atual'])

def limpar_tudo():
    estado_calculadora['valor_atual'] = 0
    estado_calculadora['expressao_atual'] = ''
    estado_calculadora['ultimo_valor'] = None
    estado_calculadora['ultima_operacao'] = None
    print(estado_calculadora['expressao_atual'])

def limpar_ultimo_numero():
    estado_calculadora['expressao_atual'] = estado_calculadora['expressao_atual'][:-1]
    print(estado_calculadora['expressao_atual'])


def calculadora():
    print("Bem-vindo(a) à calculadora!")
    print("Selecione uma opção:")
    print("1 - % (Calcula a percentagem de um valor)")
    print("2 - CE (Limpa o último valor inserido)")
    print("3 - C (Limpa todo o cálculo inserido)")
    print("4 - X (Limpa último valor inserido)")
    print("5 - 1/x (Calcula o inverso do valor inserido)")
    print("6 - x² (eleva o número inserido ao quadrado)")
    print("7 - √x (calcula a raiz quadrada do valor inserido)")
    print("8 - ÷ (Divide dois valores)")
    print("9 - × (Multiplica dois valores)")
    print("10 - - (Subtrai dois valores)")
    print("11 - + (Soma dois valores)")
    print("12 - +/-(Transforma um valor positivo em negativo e vice-versa)")
    print("13 - (Cálcula vários valores +, -, ÷, *)")
    print("Sair - Escreva Sair")



    while True:
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            valor = float(input("Insira o valor a ser calculado a porcentagem: "))
            porcentagem = float(input("Insira a porcentagem a ser calculada: "))
            resultado = valor * (porcentagem / 100)
            estado_calculadora['valor_atual'] = resultado
            estado_calculadora['expressao_atual'] = str(resultado)
            print("Resultado: ", resultado)

        elif opcao == "2":
            limpar_ultimo_valor()

        elif opcao == "3":
            limpar_tudo()

        elif opcao == "4":
            limpar_ultimo_numero()

        elif opcao == "5":
            valor = float(input("Insira o valor a ser calculado o inverso: "))
            resultado = 1 / valor
            estado_calculadora['valor_atual'] = resultado
            estado_calculadora['expressao_atual'] = str(resultado)
            print("Resultado: ", resultado)

        elif opcao == "6":
            valor = float(input("Insira o valor a ser elevado ao quadrado: "))
            resultado = valor ** 2
            estado_calculadora['valor_atual'] = resultado
            estado_calculadora['expressao_atual'] = str(resultado)
            print("Resultado: ", resultado)

        elif opcao == "7":
            valor = float(input("Insira o valor a ser calculada a raiz quadrada: "))
            resultado = valor ** 0.5
            estado_calculadora['valor_atual'] = resultado
            estado_calculadora['expressao_atual'] = str(resultado)
            print("Resultado: ", resultado)

        elif opcao == "8":
            valor1 = float(input("Insira o primeiro número: "))
            valor2 = float(input("Insira o segundo número: "))
            resultado = valor1 / valor2
            estado_calculadora['ultimo_valor'] = valor2
            estado_calculadora['ultima_operacao'] = '/'
            estado_calculadora['valor_atual'] = resultado
            estado_calculadora['expressao_atual'] += str(valor1) + ' / ' + str(valor2)
            print("Resultado: ", resultado)

        elif opcao == "9":
            valor1 = float(input("Insira o primeiro número: "))
            valor2 = float(input("Insira o segundo número: "))
            resultado = valor1 * valor2
            estado_calculadora['ultimo_valor'] = valor2
            estado_calculadora['ultima_operacao'] = '*'
            estado_calculadora['valor_atual'] = resultado
            estado_calculadora['expressao_atual'] += str(valor1) + ' * ' + str(valor2)
            print("Resultado: ", resultado)

        elif opcao == "10":
            valor1 = float(input("Insira o primeiro número: "))
            valor2 = float(input("Insira o segundo número: "))
            resultado = valor1 - valor2
            estado_calculadora['ultimo_valor'] = valor2
            estado_calculadora['ultima_operacao'] = '-'
            estado_calculadora['valor_atual'] = resultado
            estado_calculadora['expressao_atual'] += str(valor1) + ' - ' + str(valor2)
            print("Resultado: ", resultado)

        elif opcao == "11":
            valor1 = float(input("Insira o primeiro número: "))
            valor2 = float(input("Insira o segundo número: "))
            resultado = valor1 + valor2
            estado_calculadora['ultimo_valor'] = valor2
            estado_calculadora['ultima_operacao'] = '+'
            estado_calculadora['valor_atual'] = resultado
            estado_calculadora['expressao_atual'] += str(valor1) + ' + ' + str(valor2)
            print("Resultado: ", resultado)

        elif opcao == "12":
            valor = float(input("Insira o valor a ser transformado em positivo/negativo: "))
            resultado = valor * -1
            estado_calculadora['valor_atual'] = resultado
            estado_calculadora['expressao_atual'] = str(resultado)
            print("Resultado: ", resultado)

        elif opcao == "13":
            valor = input("Insira a operação matemática (ex: 2+2=): ")
            if "=" in valor:
                resultado = eval(valor[:-1])
                estado_calculadora['valor_atual'] = resultado
                estado_calculadora['expressao_atual'] = str(resultado)
                print("Resultado: ", resultado)
            else:
                print("Operação inválida! Insira o simbolo = para obter o resultado")

        elif opcao == "Sair":
            print("Encerrar a calculadora...")
            break

        else:
            print("Opção inválida. Por favor, tente novamente.")
calculadora()