#Crie uma lista chamada COMPRAS com pelo menos 5 itens. 
#Adicione um novo item à lista de forma que usuário dogote

produtos = ["Água", "Gás", "Pastilha", "Coxinha"]
print("Lista inicial: ", produtos)
resposta = input("Digite um produto: ")

produtos.append("Resposta") #adiciona no fim da lista
print("Lista atualizado: ", produtos)