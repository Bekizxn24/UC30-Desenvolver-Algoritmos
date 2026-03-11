#Questão 8

valorCompra = float(input("Digite o valor da compra: "))

if valorCompra < 100:
    desconto = 0
elif valorCompra < 500:
    desconto = valorCompra * 0.05
elif valorCompra < 1000:
    desconto = valorCompra * 0.10
else: 
    desconto = valorCompra * 0.15

    valorFinal = valorCompra - desconto

print("Valor original: R$", valorCompra)
print("Desconto: R$", desconto)
print("Valor final: R$", valorFinal)