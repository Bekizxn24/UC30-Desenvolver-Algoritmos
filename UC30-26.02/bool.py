#resp = input("Você vai passar de ano? s/N: ")
#resultado = bool(resp)

#print("Resposta ", resp)
#print("Resultado ", resultado)

resp = input("Você vai passar de ano? s/N: ").strip().lower()

resultado = (resp == "s")

print("Resultado ", resultado )
print(type(resultado))
