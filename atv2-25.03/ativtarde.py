def calcular_estatisticas(*notas):
    if not notas:
        return 0,0,0,0

    soma = sum(notas)
    media = soma / len(notas)
    maior = max(notas)
    menor = min(notas)

    return soma, media, maior, menor

soma, media, max_nota, min_nota = calcular_estatisticas(7, 8, 9)
print(f"média: {media}")