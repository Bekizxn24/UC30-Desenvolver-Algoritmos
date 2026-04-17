# Você tem uma lista de nomes de amigos em uma festa. Some a quantidade de amigos e verifique se é par ou ímpar com if-else.

amigos = ["Rebecca", "Lidia", "Vivianne", "Marcos", "Mariah", "Sophia"]

quantidade = len(amigos)

print(f"Total de amigos: {quantidade}")

if quantidade % 2 == 0:
    print("A quantidade de amigos é par.")
else:
    print("A quantidade de amigos é ímpar.")
