#Em uma eleição escolar, crie um programa que leia a idade de um aluno e diga se ele pode votar: se >= 16 anos, "Pode votar!"; senão, "Ainda não pode votar.".

idade = int(input("Digite a sua idade: "))

if idade >= 16:
    print("Pode votar!")
else:
    print("Ainda não pode votar.")
