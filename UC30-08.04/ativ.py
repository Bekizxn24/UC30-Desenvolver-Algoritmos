print("Vamos calcular quantos pontos a equipe conseguiu!")


P = int(input("Digite o número de pães vendidos: "))
D = int(input("Digite o número de doces vendidos: "))
B = int(input("Digite o número de bolos vendidos: "))

pontos = P * 1 + D * 2 + B * 3
print(f"\nA pontuação total da semana foi: {pontos} pontos")


if pontos >= 150:
    print(" A equipe ganhou um bolo como prêmio! 🎂")
    print("Resultado final: B")
elif pontos >= 120:
    print(" A equipe ganhou um doce como prêmio! 🍬")
    print("Resultado final: D")
elif pontos >= 100:
    print(" A equipe ganhou um pão como prêmio! 🍞")
    print("Resultado final: P")
else:
    print("Infelizmente não foi dessa vez, não há prêmio dessa vez. 😕")
    print("Resultado final: N")