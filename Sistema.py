# Sistema de Agendamento com Prioridade

fila_prioritaria = []
fila_normal = []

def validar_sn(resposta):
    while resposta not in ["S", "N"]:
        resposta = input("Digite apenas S ou N: ").upper()
    return resposta

def cadastrar_pessoa():
    nome = input("Nome: ")
    
    while True:
        try:
            idade = int(input("Idade: "))
            if idade < 0:
                print("Idade inválida!")
            else:
                break
        except:
            print("Digite um número válido!")

    deficiencia = validar_sn(input("Possui deficiência? (S/N): ").upper())
    gestante = validar_sn(input("Está gestante? (S/N): ").upper())

    prioridade = False

    if idade >= 60 or deficiencia == "S" or gestante == "S":
        prioridade = True

    pessoa = {
        "nome": nome,
        "idade": idade,
        "prioridade": prioridade
    }

    if prioridade:
        fila_prioritaria.append(pessoa)
    else:
        fila_normal.append(pessoa)

def mostrar_fila():
    print("\n=== FILA DE ATENDIMENTO ===")

    print("\nPrioridade:")
    for p in fila_prioritaria:
        print(f"{p['nome']} ({p['idade']} anos)")

    print("\nNormal:")
    for p in fila_normal:
        print(f"{p['nome']} ({p['idade']} anos)")

def menu():
    while True:
        print("\n1 - Cadastrar pessoa")
        print("2 - Mostrar fila")
        print("3 - Sair")

        opcao = input("Escolha: ")

        if opcao == "1":
            cadastrar_pessoa()
        elif opcao == "2":
            mostrar_fila()
        elif opcao == "3":
            print("Encerrando...")
            break
        else:
            print("Opção inválida!")

menu()