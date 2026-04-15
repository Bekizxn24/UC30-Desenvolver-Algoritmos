def soma_segura(a, b):
    try:
        resultado = a + b
        return resultado
    except TypeError:
        print("Entrada inválida")
        return 0

# Testes
print(soma_segura(10, 5))      
print(soma_segura(10, "5"))    
