#Questão 7

senha = input("Digite a senha: ")

temSenha = any(caractere.isdigit() for caractere in senha)

if len(senha) >= 8 and temSenha:
    print("Senha válida!")
else: 
    print("Senha inválida!")