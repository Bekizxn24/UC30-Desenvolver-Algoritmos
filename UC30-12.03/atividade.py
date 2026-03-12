#Gere uma função que mostra a soma e o produto de dois números

def calcular_soma_produto(a, b):
    soma = a + b
    produto = a * b 

    resultado_soma, resultado_produto = calcular_soma_produto(4, 6)
    print(f"Soma: {resultado_soma}, Produto: {resultado_produto}")