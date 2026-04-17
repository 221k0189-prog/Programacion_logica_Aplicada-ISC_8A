###
# EJERCICIOS (while)
###
from os import system
if system("clean") !=0: system("cls")

#Ejercicio 1: Cuenta atrás.
#Imprime los números del 10 al 1 usando un bucle while.
print("\nEjercicio 1: Cuenta atras")

contador = 10

while contador >= 1:
    print(contador)
    contador -=1

#Ejercicio 2: Suma de números pares (while)
#Calcula la suma de los números pares entre 1 y 20 (inclusive) usando un bucle while.
print("\nEjercicio 2: Suma de números pares")

suma = 0
numero = 1

while numero <= 20:
    if numero % 2 == 0:
        suma += numero
    numero += 1

print(f"La suma de los numeros pares es: {suma}")

#Ejercicio 3: Factorial de un número
#Pide al usuario que introduzca un número entero positivo.
#Calcula su factorial usando un bucle while.
#El factorial de un número entero positivo es el producto de todos los números del 1 al ese número. Por ejemplo, el factorial de 5
# 5! = 5 * 4 * 3 * 2 * 1 = 128
print("\nEjercicio 3: Factorial de un número")

n = int(input("Introdusca un nummero entero positivo: "))

factorial = 1
i = 1
while i <= n:
    factorial *= i
    i += 1

print(f"El factorial de {n} es: {factorial}")

#Ejercicio 4: Validación de contraseña
# Pide al usuario que introduzca una contraseña.
# La contraseña debe tener al menos 8 caracteres.
#Usa un bucle while para seguir pidiendo la contraseña hasta que cumpla con los requisitos.
#Si la contraseña es válida, imprime "Contraseña válida".
print("\nEjercicio 4: Validación de contraseña")

contraseña = ""

while len(contraseña) < 8:
    contraseña = input("Introdusca una contrseña (minimo 8 caracteres): ")

print("Contraseña valida")

#Ejercicio 5: Tabla de multiplicar
# Pide al usuario que introduzca un número.
#Imprime la tabla de multiplicar de ese número (del 1 al 10) usando un bucle while.
print("\nEjercicio 5: Tabla de multiplicar")

num = int(input("Introdusca un numero: "))

a = 1
while a <= 10:
    print(f"{num} x {a} = {num * a}")
    a += 1

# Ejercicio 6: Números primos hasta N
#Pide al usuario que introduzca un número entero positivo Ν.
# Imprime todos los números primos menores o iguales que N usando un bucle while.
print("\nEjercicio 6: Números primos hasta N")

n = int(input("Introdusca un numero entero: "))

num = 2

while num <= n:
    es_primo = True
    divisor = 2
    while divisor * divisor <= num:
        if num % divisor == 0:
            es_primo = False
            break
        divisor += 1
    if es_primo:
        print(num)
    num += 1