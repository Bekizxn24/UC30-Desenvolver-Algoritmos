#Conte vogais em uma frase digitada pelo usuário (ex: análise de texto para rede social).

def contar_vogais(frase):
    vogais = "aeiouAEIOU"
    mapa_de_acentos = str.maketrans("áéíóúâêîôûãõàèìòù", "aeiouaeiouaoaeiou")
    frase_limpa = frase.translate(mapa_de_acentos)
    
    contador = sum(1 for letra in frase_limpa if letra in vogais)
    return contador

texto = input("Digite sua frase: ")
print(f"A frase possui {contar_vogais(texto)} vogais.")
