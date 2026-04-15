fila_prioritaria = []
fila_normal = []

# ================= VALIDAÇÕES =================
def validar_sn(msg):
    while True:
        resp = input(msg).upper()
        if resp in ["S", "N"]:
            return resp
        print("Digite apenas S ou N!")

def validar_int(msg):
    while True:
        try:
            valor = int(input(msg))
            if valor < 0:
                print("Valor inválido!")
            else:
                return valor
        except:
            print("Digite um número válido!")

# ================= CADASTRO =================
def cadastrar_pessoa():
    print("\n=== CADASTRAR PESSOA ===")
    
    nome = input("Nome: ")
    idade = validar_int("Idade: ")
    deficiencia = validar_sn("Possui deficiência? (S/N): ")
    gestante = validar_sn("Está gestante? (S/N): ")

    prioridade = idade >= 60 or deficiencia == "S" or gestante == "S"

    pessoa = {
        "nome": nome,
        "idade": idade,
        "prioridade": prioridade
    }

    if prioridade:
        fila_prioritaria.append(pessoa)
        print("✅ Adicionado à FILA PRIORITÁRIA!")
    else:
        fila_normal.append(pessoa)
        print("✅ Adicionado à fila normal!")

# ================= MOSTRAR FILA =================
def mostrar_fila():
    print("\n=== FILA DE ATENDIMENTO ===")

    print(f"\n🔴 Prioridade ({len(fila_prioritaria)} pessoas):")
    for i, p in enumerate(fila_prioritaria, 1):
        print(f"{i}. {p['nome']} ({p['idade']} anos)")

    print(f"\n🟢 Normal ({len(fila_normal)} pessoas):")
    for i, p in enumerate(fila_normal, 1):
        print(f"{i}. {p['nome']} ({p['idade']} anos)")

# ================= ATENDER =================
def atender_proximo():
    print("\n=== ATENDIMENTO ===")

    if fila_prioritaria:
        pessoa = fila_prioritaria.pop(0)
        print(f"🔴 Atendendo (PRIORIDADE): {pessoa['nome']}")
    elif fila_normal:
        pessoa = fila_normal.pop(0)
        print(f"🟢 Atendendo: {pessoa['nome']}")
    else:
        print("Fila vazia!")

# ================= BUSCAR =================
def buscar_pessoa():
    nome = input("Digite o nome para buscar: ").lower()

    for p in fila_prioritaria:
        if p["nome"].lower() == nome:
            print(f"Encontrado na FILA PRIORITÁRIA: {p['nome']}")
            return

    for p in fila_normal:
        if p["nome"].lower() == nome:
            print(f"Encontrado na fila normal: {p['nome']}")
            return

    print("Pessoa não encontrada!")

# ================= REMOVER =================
def remover_pessoa():
    nome = input("Digite o nome para remover: ").lower()

    for fila in [fila_prioritaria, fila_normal]:
        for p in fila:
            if p["nome"].lower() == nome:
                fila.remove(p)
                print("Pessoa removida com sucesso!")
                return

    print("Pessoa não encontrada!")

# ================= LIMPAR FILAS =================
def limpar_filas():
    confirmacao = validar_sn("Tem certeza que deseja limpar todas as filas? (S/N): ")
    
    if confirmacao == "S":
        fila_prioritaria.clear()
        fila_normal.clear()
        print("Filas limpas com sucesso!")
    else:
        print("Operação cancelada.")

# ================= MENU =================
def menu():
    while True:
        print("\n====== SISTEMA DE ATENDIMENTO ======")
        print("1 - Cadastrar pessoa")
        print("2 - Mostrar filas")
        print("3 - Atender próxima pessoa")
        print("4 - Buscar pessoa")
        print("5 - Remover pessoa")
        print("6 - Limpar filas")
        print("7 - Sair")

        opcao = input("Escolha: ")

        if opcao == "1":
            cadastrar_pessoa()
        elif opcao == "2":
            mostrar_fila()
        elif opcao == "3":
            atender_proximo()
        elif opcao == "4":
            buscar_pessoa()
        elif opcao == "5":
            remover_pessoa()
        elif opcao == "6":
            limpar_filas()
        elif opcao == "7":
            print("Encerrando sistema...")
            break
        else:
            print("Opção inválida!")

menu()