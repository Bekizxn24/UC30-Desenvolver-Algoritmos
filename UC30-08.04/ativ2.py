n = int(input("Digite o número inicial de pessoas infectadas: "))
r = int(input("Digite a taxa de multiplicação diária: "))
p = int(input("Digite o número de pessoas: "))

total = n
novos = n 
dias = 0 

print(f"Começamos com o número de {total} pessoas infectadas no dia zero.")

while total < p:
    dias = dias + 1 
    novos = novos * r 
    total = total + novos
    print(f"No dia {dias} mais {novos} pessoas se infectaram, chegando a um total de {total} pessoas.")

print(f"Serão necessários {dias} dias para atongor ou ultrapassar o número alvo.")