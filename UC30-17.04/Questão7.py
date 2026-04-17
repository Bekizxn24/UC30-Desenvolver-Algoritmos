# Em uma lista de números de vendas de uma loja, use for para somar apenas os valores pares e imprimir o resultado.

vendas = [101, 50, 250, 31, 12, 80, 104]

soma_pares = 0

for venda in vendas:
    if venda % 2 == 0:
        soma_pares += venda 

print(f"Lista de vendas: {vendas}")
print(f"Soma apenas dos valores pares: {soma_pares}")
