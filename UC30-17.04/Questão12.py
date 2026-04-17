#Crie um menu simples de calculadora com while: 1-soma, 2-subtração,3-multiplicação, 4-divisão, 5-sair. Use if-else e try-except.

def calculadora():
    while True:
        print("\nMenu Calculadora")
        print("1 - Soma")
        print("2 - Subtração")
        print("3 - Multiplicação")
        print("4 - Divisão")
        print("5 - Sair")
        
        opcao = input("Escolha uma opção (1-5): ")

        if opcao == '5':
            print("Saindo da calculadora. Até mais!")
            break
        
        if opcao in ('1', '2', '3', '4'):
            try:
                num1 = float(input("Digite o primeiro número: "))
                num2 = float(input("Digite o segundo número: "))
                
                if opcao == '1':
                    resultado = num1 + num2
                    print(f"Resultado: {num1} + {num2} = {resultado}")
                elif opcao == '2':
                    resultado = num1 - num2
                    print(f"Resultado: {num1} - {num2} = {resultado}")
                elif opcao == '3':
                    resultado = num1 * num2
                    print(f"Resultado: {num1} * {num2} = {resultado}")
                elif opcao == '4':
                    if num2 == 0:
                        print("Erro: Divisão por zero não é permitida.")
                    else:
                        resultado = num1 / num2
                        print(f"Resultado: {num1} / {num2} = {resultado}")
            
            except ValueError:
                print("Erro: Inválido. Por favor, digite apenas números.")
        else:
            print("Inválido! Tente novamente.")

calculadora()
