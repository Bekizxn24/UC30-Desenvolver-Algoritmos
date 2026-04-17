# No supermercado, um cliente quer somar o valor de itens até digitar 0. Use while para ler valores (float) e imprimir o total final.

total = 0.0
valor = -1 

print("Digite os valores dos itens (digite 0 para encerrar):")

while True:
    try:
        valor = float(input("Digite o valor do item: R$ "))
        
        if valor == 0:
            break
        
        total += valor
        print(f"Subtotal: R$ {total:.2f}")
        
    except ValueError:
        print("Inválido. Por favor, digite um número.")

print("-" * 30)
print(f"Total final da compra: R$ {total:.2f}")
print("Obrigado pela confiança e preferência!")
