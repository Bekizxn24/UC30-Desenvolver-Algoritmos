#Em uma loja online, aplique desconto: >500 reais = 20%, 200-500=10%, <200=nenhum. Leia valor e imprima preço final.

valor_compra = float(input("Digite o valor total da compra: R$ "))

if valor_compra > 500:
    desconto = 0.20
elif valor_compra >= 200:
    desconto = 0.10
else:
    desconto = 0.0

preco_final = valor_compra * (1 - desconto)

print(f"Valor original: R$ {valor_compra:.2f}")
print(f"Desconto aplicado: {desconto*100:.0f}%")
print(f"Preço final: R$ {preco_final:.2f}")
