import json
import os

ARQUIVO = "dados.json"

fila_prioritaria = []
fila_normal = []
historico = []

# ================== ARQUIVO ==================

def salvar_dados():
    dados = {
        "prioritaria": fila_prioritaria,
        "normal": fila_normal,
        "historico": historico
    }
    with open(ARQUIVO, "w") as f:
        json.dump(dados, f, indent=4)

def carregar_dados():
    global fila_prioritaria, fila_normal, historico

    if os.path.exists(ARQUIVO):
        with open(ARQUIVO, "r") as f:
            dados = json.load(f)
            fila_prioritaria = dados.get("prioritaria", [])
            fila_normal = dados.get("normal", [])
            historico = dados.get("historico", [])

# ================== VALIDAÇÕES ==================

def validar_sn(msg):
    while True:
        resp = input(msg).strip().lower()
        if resp in ["s", "sim"]:
            return True
        elif resp in ["n", "nao", "não"]:
            return False
        print("Digite S/Sim ou N/Não!")

def validar_int(msg):
    while True:
        try:
            valor = int(input(msg))
            if valor < 0:
                print("Valor inválido!")
            else:
                return valor
        except ValueError:
            print("Digite um número válido!")

def validar_cpf():
    while True:
        cpf = input("CPF (11 números): ").strip()

        if not cpf.isdigit() or len(cpf) != 11:
            print("CPF inválido!")
            continue

        if buscar_por_cpf(cpf, mostrar=False):
            print("CPF já cadastrado!")
            continue

        return cpf

# ================== FUNÇÕES ==================

def cadastrar():
    print("\n=== CADASTRO ===")

    nome = input("Nome: ").strip()
    cpf = validar_cpf()
    idade = validar_int("Idade: ")
    deficiencia = validar_sn("Possui deficiência? (S/N): ")
    gestante = validar_sn("Gestante? (S/N): ")

    prioridade = idade >= 60 or deficiencia or gestante

    pessoa = {
        "nome": nome,
        "cpf": cpf,
        "idade": idade,
        "prioridade": prioridade
    }

    if prioridade:
        fila_prioritaria.append(pessoa)
    else:
        fila_normal.append(pessoa)

    salvar_dados()
    print("✅ Pessoa cadastrada!")

def listar():
    print("\n=== FILAS ===")

    print("\n🔴 PRIORIDADE:")
    for p in fila_prioritaria:
        print(f"{p['nome']} | CPF: {p['cpf']}")

    print("\n🟢 NORMAL:")
    for p in fila_normal:
        print(f"{p['nome']} | CPF: {p['cpf']}")

def atender():
    print("\n=== ATENDIMENTO ===")

    if fila_prioritaria:
        pessoa = fila_prioritaria.pop(0)
    elif fila_normal:
        pessoa = fila_normal.pop(0)
    else:
        print("Fila vazia!")
        return

    historico.append(pessoa)
    salvar_dados()

    print(f"Atendendo: {pessoa['nome']}")

def buscar_por_cpf(cpf=None, mostrar=True):
    if not cpf:
        cpf = input("CPF: ")

    for p in fila_prioritaria + fila_normal:
        if p["cpf"] == cpf:
            if mostrar:
                print(f"Encontrado: {p['nome']}")
            return p

    if mostrar:
        print("Não encontrado!")
    return None

def remover():
    cpf = input("CPF para remover: ")

    for fila in [fila_prioritaria, fila_normal]:
        for p in fila:
            if p["cpf"] == cpf:
                fila.remove(p)
                salvar_dados()
                print("Removido!")
                return

    print("Não encontrado!")

def editar():
    cpf = input("CPF para editar: ")
    pessoa = buscar_por_cpf(cpf, mostrar=False)

    if not pessoa:
        print("Pessoa não encontrada!")
        return

    print("Deixe vazio para não alterar")

    novo_nome = input("Novo nome: ")
    if novo_nome:
        pessoa["nome"] = novo_nome

    salvar_dados()
    print("Atualizado!")

def tempo_espera():
    total = len(fila_prioritaria) + len(fila_normal)
    tempo = total * 5
    print(f"Tempo estimado: {tempo} minutos")

def ver_historico():
    print("\n=== HISTÓRICO ===")
    for p in historico:
        print(f"{p['nome']} | CPF: {p['cpf']}")

# ================== MENU ==================

def menu():
    carregar_dados()

    while True:
        print("\n===== SISTEMA =====")
        print("1 - Cadastrar")
        print("2 - Listar filas")
        print("3 - Atender")
        print("4 - Buscar")
        print("5 - Remover")
        print("6 - Editar")
        print("7 - Tempo de espera")
        print("8 - Histórico")
        print("9 - Sair")

        op = input("Opção: ")

        if op == "1":
            cadastrar()
        elif op == "2":
            listar()
        elif op == "3":
            atender()
        elif op == "4":
            buscar_por_cpf()
        elif op == "5":
            remover()
        elif op == "6":
            editar()
        elif op == "7":
            tempo_espera()
        elif op == "8":
            ver_historico()
        elif op == "9":
            print("Saindo...")
            break
        else:
            print("Opção inválida!")

menu()
