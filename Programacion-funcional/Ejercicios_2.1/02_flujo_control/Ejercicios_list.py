###
# EJERCICIOS
###

# Ejercicio 1: El mensaje secreto
# Dada la siguiente lista:
# mensaje = ["C", "o", "d", "i", "g", "o", " ", "s", "e", "c", "r", "e", "t", "o"]
# Utilizando slicing y concatenación, crea una nueva lista que contenga solo el mensaje "secreto".
print("\nEjercicio 1: El mensaje secreto")

mensaje = ["c", "o", "d", "i", "g", "o", " ", "s", "e", "c", "r", "e", "t", "o"]

secreto = mensaje[7:]

print("El resultado es: ", secreto)

# Ejercicio 2: Intercambio de posiciones
# Dada la siguiente lista:
# numeros = [10, 20, 30, 40, 50]
# Intercambia la primera y la última posición utilizando solo asignación por índice.
print("\nEjercicio 2: Intercambio de posiciones")

numeros = [10, 20, 30, 40, 50]

intercambio = numeros[0]
numeros[0] = numeros[4]
numeros[4] = intercambio


print("El resultado es: ", numeros)

# Ejercicio 3: El sándwich de listas
# Dadas las siguientes listas:
# pan = ["pan arriba"]
# ingredientes = ["jamón", "queso", "tomate"]
# pan_abajo = ["pan abajo"]
# Crea una lista llamada sandwich que contenga el pan de arriba, los ingredientes y el pan de abajo, en ese orden.
print("\nEjercicio 3: El sánwich de listas")

pan = ["pan arriba"]
ingredientes = ["jamón", "queso", "tomate"]
pan_abajo = ["pan abajo"]

sandwich = pan + ingredientes + pan_abajo

print("El resultado es: ", sandwich)

# Ejercicio 4: Duplicando la list
# Dada una lista:
# lista = [1, 2, 3]
# Crea una nueva lista que contenga los elementos de la lista original duplicados.
# Ejemplo: [1, 2, 3] -> [1, 2, 3, 1, 2, 3]
print("\nEjercicio 4: Duplicando la lista")

lista = [1, 2, 3]

nueva_lista = lista + lista

print("El resultado es: ", nueva_lista)

# Ejercicio 5: Extrayendo el centro
# Dada una lista con un número impar de elementos, extrae el elemento que se encuentra en el centro de la lista utilizando slicing.
# Ejemplo: lista = [10, 20, 30, 40, 50] -> El centro es 30
print("\n Ejercicio 5: Extrayendo el centro")

lista2 = [10, 20, 30, 40, 50]

centro_lista = lista2[2] 

print("El centro es: ", centro_lista)

# Ejercicio 6: Reversa parcial
# Dada una lista, invierte solo la primera mitad de la lista (utilizando slicing y concatenación).
# Ejemplo: lista = [1, 2, 3, 4, 5, 6] -> Resultado: [3, 2, 1, 4, 5, 6]
print("\nEjercicio 6: Reserva parcial")

lista3 = [1, 2, 3, 4, 5, 6]

mitad1 = lista3[:3]
mitad2 = lista3[3:]

mitad1 = mitad1[::-1]

resultado = mitad1 + mitad2

print("El resultado es: ", resultado)