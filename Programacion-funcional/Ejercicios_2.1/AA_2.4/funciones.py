# EJEMPLO CALLBACK
def operar(n1, n2, funcion):
    return funcion(n1, n2)

def suma(a, b):
    return a + b

def resta(a, b):
    return a - b 

resultado = operar(5, 3, suma)

print()


#funcion de primera clase

## funcion de callback que se pasa 