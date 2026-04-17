#Registre 7 temperaturas diárias da semana em uma lista e calcule/imprima a média usando for.

temperaturas = [17.5, 20.0, 19.5, 23.0, 27.5, 26.0, 21.0]

soma_temperaturas = 0.0
contador = 0

for temp in temperaturas:
    soma_temperaturas += temp
    contador += 1

media = soma_temperaturas / contador

print(f"Temperaturas registradas: {temperaturas}")
print(f"A temperatura média da semana é: {media:.2f}°C")
