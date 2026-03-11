#Questao 12

total = 0 
quantidade = 0 

while True: 
    deposito = float(input("Digite o valor do dpósito(0 para encerrar): "))

    if deposito == 0: 
        break

    total+= deposito
    quantidade += 1 

print("Total dpositado:", total)
print("Quantidade de transações:", quantidade)