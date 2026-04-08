print("Vamos calcular quantos pontos a equipe conseguiu!")


p = int(input("Digite o número de pães vendidos: "))
d = int(input("Digite o número de doces vendidos: "))
b = int(input("Digite o número de bolos vendidos: "))

pontos = p * 1 + d * 2 + b * 3
print(f"\nA pontuação total da semana foi: {pontos} pontos")


if pontos >= 150:
    print(" A equipe ganhou um bolo como prêmio! 🎂")
    print("Resultado final: b")
elif pontos >= 120:
    print(" A equipe ganhou um doce como prêmio! 🍬")
    print("Resultado final: d")
elif pontos >= 100:
    print(" A equipe ganhou um pão como prêmio! 🍞")
    print("Resultado final: p")
else:
    print("Infelizmente não foi dessa vez, não há prêmio dessa vez. 😕")
    print("Resultado final: n")
