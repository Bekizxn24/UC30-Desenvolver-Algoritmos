# Em uma lista de notas de alunos, conte quantas estão acima de 7 e imprima o resultado usando for e if.

notas = [5.9, 8.0, 6.0, 9.7, 7.0, 2.0, 9.9, 7.5, 4.0]

contador = 0

for nota in notas:
    if nota > 7:
        contador += 1

print(f"Quantidade de notas acima de 7: {contador}")
