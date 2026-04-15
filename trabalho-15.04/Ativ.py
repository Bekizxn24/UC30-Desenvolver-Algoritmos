def soma_segura (a, b):
    try:
        soma = a + b
        return soma
    except TypeError:
        print ("Entrada inválida!")
        return 0


def divisao (x, y):
    try:
        quociente = x / y
        return quociente
    except ZeroDivisionError:
        return "Não da pra dividir por zero!"
