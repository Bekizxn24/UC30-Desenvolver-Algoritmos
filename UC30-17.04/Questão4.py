#Crie uma função que receba o peso e altura de uma pessoa (para academia) e categorize o IMC: magro (24.9). Use if-else e try-except para entradas inválidas.

def categorizar_imc_academia():
    try:
        peso = float(input("Digite o seu peso (kg): "))
        altura = float(input("Digite a sua altura (m): "))

        if peso <= 0 or altura <= 0:
            print("Inválido: Peso e altura devem ser números positivos.")
            return

        imc = peso / (altura ** 2)
        print(f"\nSeu IMC é: {imc:.2f}")

        if imc < 18.5:
            print("Classificação: Abaixo do peso (Magro).")
        elif 18.5 <= imc < 24.9:
            print("Classificação: Peso Ideal/Saudável.")
        elif 24.9 <= imc < 30.0:
            print("Classificação: Sobrepeso (Atenção academia).")
        else:
            print("Classificação: Obesidade (Busque acompanhamento).")

    except ValueError:
        print("Erro: Entrada inválida. Por favor, use números e ponto para decimais (ex: 1.75).")

if __name__ == "__main__":
    categorizar_imc_academia()
