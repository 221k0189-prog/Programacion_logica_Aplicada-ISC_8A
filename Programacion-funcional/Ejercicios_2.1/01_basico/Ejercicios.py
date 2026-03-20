# exercises.py
# Ejercicios para practicar los conceptos aprendidos en las lecciones.
###

from os import system
if system("clear") != 0: system("cls")

print("\nEjercicio 1: Imprimir mensajes")
print("Escribe un programa que imprima tu nombre y tu ciudad en líneas separadas.")

### Completa aquí
print("Angel")
print("FCP")

print("\nEjercicio 2: Muestra los tipos de datos de las siguientes variables:")
print("Usa el comando 'type()' para determinar el tipo de datos de cada variable.")

a = 15
b = 3.14159
c = "Hola mundo"
d = True
e = None

### Completa aquí
print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))

print("\nEjercicio 3: Casting de tipos")
print("Convierte la cadena '12345' a un entero y luego a un float.")
print("Convierte el float 3.14159 a un entero. ¿Qué ocurre?")

### Completa aquí
entero = int(12345)
flota = float(entero)

print(entero)
print(flota)

enter1 = int(3.1416)
print(enter1)

print("\nEjercicio 4: Variables")
print("Crea variables para tu nombre, edad y altura.")
print("Usa f-strings para imprimir una presentación.")

print("¡Hola! Me llamo tu_nombre y tengo tu_edad años, mido tu_altura metros")

### Completa aquí
nombre = "Angel"
edad = 21
altura = 1.68

print(f"¡Hola! Me llamo {nombre}, y tengo {edad}, mido {altura} metros")

print("\nEjercicio 5: Números")
print("1. Crea una variable con el número PI (sin asignar una variable)")
print("2. Redondea el número con round()")
print("3. Haz la división entera entre el número que te salió y el número 2")
print("4. El resultado debería ser 1")

### Completa aquí
variable = round(3.14159)
division = variable // 2
print(division)