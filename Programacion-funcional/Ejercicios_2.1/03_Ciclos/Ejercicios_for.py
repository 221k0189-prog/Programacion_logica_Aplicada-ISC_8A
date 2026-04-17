###
# EJERCICIOS (for)
###

from os import system
if system("clean") !=0: system("cls")

# Ejercicio 1: Imprimir números pares
# Imprime todos los números pares del 2 al 20 (inclusive) usando un bucle for.
print("\nEjercicio 1: Imprimir números pares")

for num in range(2, 21):
    if num % 2 == 0:
        print(num)

#Ejercicio 2: Calcular la media de una lista
# Dada la siguiente lista de números:
#numeros = [10, 20, 30, 40, 50]
# Calcula la media de los números usando un bucle for.
print("\nEjercicio 2: Calcular la media de una lista")

numeros = [10, 20, 30, 40, 50]
suma = 0

for n in numeros:
    suma += n

media = suma / len(numeros)

print(f"La media es: {media}")

# Ejercicio 3: Buscar el máximo de una lista
#Dada la siguiente lista de números:
#numeros = [15, 5, 25, 10, 20]
#Encuentra el número máximo en la lista usando un bucle for.
print("\nEjercicio 3: Buscar el máximo de una lista")

numeros = [15, 5, 25, 10, 20]
maximo = numeros[0]

for n in numeros:
    if n > maximo:
        maximo = n

print(f"El numero maximo es: {maximo}")

# Ejercicio 4: Filtrar cadenas por longitud
#Dada la siguiente lista de palabras:
# palabras = ["cerro", "carros", "miel", "abejorro", "cantarito"]
# Crea una nueva lista que contenga solo las palabras con más de 5 letras
#usando un bucle for y list comprehension.
print("\nEjercicio 4: Filtrar cadenas por longitud")

palabras = ["cerro", "carros", "miel", "abejorro", "cantarito"]
resultado_fil = []

for a in palabras:
    if len(a) > 5:
        resultado_fil.append(a)

resultado = [a for a in palabras if len(a) > 5]

print(f"Resultado: {resultado}")

#Ejercicio 5: Contar palabras que empiezan con una letra
#Dada la siguiente lista de palabras:
#palabras = ["cerro", "carros", "miel", "abejorro", "cantarito"]
# Pide al usuario que introduzca una letra.
# Cuenta cuántas palabras en la lista empiezan con esa letra (sin diferenciar mayúsculas/minúsculas).
print("\nEjercicio 5: Contar palabras que empiezan con una letra")

palabras = ["cerro", "carros", "miel", "abejorro", "cantarito"]
usuario = input("Introduce una letra: ").lower()
contador = 0

for a in palabras:
    if a.lower().startswith(usuario):
        contador += 1

print(f"Hay {contador} palabras que empiezan con la letra '{usuario}'.")