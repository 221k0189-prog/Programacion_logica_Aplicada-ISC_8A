###
# EJERCICIOS
###

# Ejercicio 1: Determinar el mayor de dos números
# Pide al usuario que introduzca dos números y muestra un mensaje
# indicando cuál es mayor o si son iguales

print("\nEjercicio 1: Determinar el mayor de dos números")

num1 = (input("Introdusca el primer número: "))
num2 = (input("Introdusca el segundo número: "))

if num1 > num2:
   print("El numero mayor es: ", num1)
elif num2 > num1:
   print("El numero mayor es:", num2)
else:
   print("Los dos numeros son iguales")

# Ejercicio 2: Calculadora simple
# Pide al usuario dos números y una operación (+, -, *, /)
# Realiza la operación y muestra el resultado (maneja la división entre cero)
print("\nEjercicio 2: Calculadora simple")

nume1 = int(input("Introdusca el primer numero: "))
nume2 = int(input("Introdusca el segundo numero: "))
operacion = input("Introdusca la operacion (+, -, *, /):")

if operacion == "+":
    print("El Resultado es:", nume1 + nume2)
elif operacion == "-":
    print("El Resultado es:", nume1 - nume2)
elif operacion == "*":
    print("El Resultado es:", nume1 * nume2)
elif operacion == "/":
   if nume2 != 0:
     print("No se puede dividir entre 0")
   else:
       print("El Resultado es:", nume1 / nume2)
else: 
   print("Operación no validad")
   

# Ejercicio 3: Año bisiesto
# Pide al usuario que introduzca un año y determina si es bisiesto.
# Un año es bisiesto si es divisible por 4, excepto si es divisible por 100 pero no por 400.

print("\nEjercicio 3: Año bisiesto")

anio = int(input("Introdusca un año: ")) 

if (anio / 4 == 0 and anio / 100 != 0) or (anio / 400 == 0):
   print("El año es bisiesto")
else:
   print("El año no es bisiesto")

# Ejercicio 4: Categorizar edades
# Pide al usuario que introduzca una edad y la clasifique en:
# - Bebé (0–2 años)
# - Niño (3–12 años)
# - Adolescente (13–17 años)
# - Adulto (18–64 años)
# - Adulto mayor (65 años o más)

print("\nEjercicio 4: Categorizar edades")

edad = int(input("Introdusca su edad: "))

if 0 <= edad <=2:
   print("Bebe")
elif 3 <= edad <= 12:
   print("Niño")
elif 13 <= edad <= 17:
   print("Adolecente")
elif 18 <= edad <= 64:
   print("Adulto mayor")
else:
   print("Edad no valida")
