#1- Controle financeiro
def controle_financeiro(mesada, gastos):
    total = 0

    for gasto in gastos:
        total += gasto

    if total > mesada: 
        print(f"Prejuízo de R${total - mesada}")
    else: 
        print(f"Sobrou R${mesada - total}")

#2- Transporte
def transporte(passagem, dias):
    total = 0 

    for i in range(dias):
        total += passagem * 2

    print(f"Gasto total do mês: R${total}")

#3- Internet
def internet(consumo):
    total = 0

    for dia in consumo: 
        total += dia

    if total > 30:
        print("Plano excedido")
    else: 
        print("Dentro do limite")