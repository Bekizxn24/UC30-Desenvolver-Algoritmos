#Atividade - Manipulação de listas em Python

numeros = [10, 20, 30, 20, 40, 20, 50]

#len: número de elementos
print("Comprimento: ", len(numeros))

#count: conta ocorrências
print("Quantas vezes o 20 aparece: ", numeros.count(20))

#encontra a posição
print("índice de 30: ", numeros.index(30))

#in: verifica a existência
print("20 está na lista? ", 20 in numeros)
print("100 está na lista? ", 100 in numeros)

import random 

numeros = [91, 34, 67, 15, 82]
print("Lista original: ", numeros)

#sort crescente
numeros.sort()
print("Após sort(): ", numeros)

#sort decrescente
numeros.sort(reverse=True)
print("Após sort(): ", numeros)

#embaralhar
dados = [91, 34, 67, 15, 82]
random.shuffle(dados)
print("Embaralhar: ", dados)

numeros2 = [15, 16, 17, 18, 19, 20]
print("Lista original: ", numeros2)

#sort crescente
numeros2.sort()
print("Após sort(): ", numeros2)

#sort decrescente
numeros2.sort(reverse=True)
print("Após sort(): ", numeros2)

#embaralhar
dados = [15, 16, 17, 18, 19, 20]
random.shuffle(dados)
print("Embaralhar: ", dados)
