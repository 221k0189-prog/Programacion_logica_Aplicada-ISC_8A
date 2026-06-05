# Ejercicio 3: Inflar globos
# Objetivo: Crea un programa que simule la inflada de globos 🎈 para una fiesta, de acuerdo al número de invitados que asistirán.

## 1.- Define una función llamada inflar_globo que no reciba parámetros
##   y devuelva el emoji de globo "🎈".
def inflar_globo():
    return "🎈"

## 2.- Crea esta misma función usando lambda y asigna el resultado a la variable inflar_globo_lambda.
inflar_globo_lambda = lambda: "🎈"

## 3.- crea una lista de globos usando la función lambda y una comprensión de listas, para el número de invitados que se ingresen por el usuario.  
numero_invitados = int(input("Cuantos invitados van a la fiesta:"))

globos_lambda = [inflar_globo_lambda() for _ in range(numero_invitados)]

## 2.- Define una función llamada preparar_globos que reciba un argumento
##    numero_invitados (entero).
##    Dentro de la función:
##   -- Usa una comprensión de listas para llamar a inflar_globo()
##       tantas veces como indique numero_invitados.
##    -- Devuelve esa lista.
def preparar_globos(numero_invitados):
    return [inflar_globo() for _ in range(numero_invitados)]

## 3.- Llama a preparar_globos solicitando al usuario ingresar el número
##    de invitados a la fiesta y almacena el resultado en una variable globos_fiesta.
globos_fiesta = preparar_globos(numero_invitados)

## 4.- Muestra en pantalla el contenido de globos_fiesta,
##    que será una lista con varios emojis "🎈".
print("\nGlobos creados con lambda:")
print(globos_lambda)

print("\nGlobos para la fiesta:")
print(globos_fiesta)

## Ejemplo de salida:
##    ¿Cuántos invitados van a la fiesta? 3
##    ['🎈', '🎈', '🎈']

    
# Ejercicio 4: Mostrar el menú de la cafetería
# Objetivo: Usar comprensión de listas para formatear y mostrar el menú de una cafetería con los precios de cada bebida.


## 1.- Crea una función llamada ver_menu que reciba un diccionario llamado menu.
def ver_menu(menu):
    return [f"{nombre.capitalize()}: ${precio:.2f}" for nombre, precio in menu.items()]

## 2.- Dentro de la función, usa comprensión de listas para recorrer menu.items().
##    Cada elemento del diccionario tiene dos partes: la clave (nombre de la bebida) y el valor (precio).
##    Estructura: for nombre, precio in menu.items()
menu = {
    "americano": 25.50,
    "café de olla": 22.00,
    "capuchino": 35.75,
    "coca": 40.00,
    "agua": 18.50
}
## 3.- Para cada par clave-valor, genera una cadena con el formato: "Americano: $25.50"
## Es decir: f"{nombre.capitalize()}: ${precio:.2f}"
## 4.- La función debe devolver la lista generada por la comprensión.
## 5.- Crea la variable menu con el diccionario de precios mostrado arriba.
## 6.- Llama a ver_menu con el diccionario menu y guarda el resultado en una variable llamada menu_formateado.
## 7.- Imprime cada elemento de menu_formateado en una línea separada usando un ciclo for.
## Salida esperada (los precios pueden variar según el diccionario):
##    Americano: $25.50
##    Café de olla: $22.00
##    Capuchino: $35.75
##    Coca: $40.00
##    Agua: $18.50

menu_formateado = ver_menu(menu)

print("\nMENÚ DE LA CAFETERÍA")
for bebida in menu_formateado:
    print(bebida)

## Ejercicio 4: La cuenta de la cafetería
## Objetivo: Dada una lista de precios de las ordenes de la cafetería y deberás aplicar varias funciones de orden superior (map, filter, reduce) para calcular el total a pagar. 
## Usa map(): Aplicar el 10% de descuento a cada precio
##----------------------------------------------------------------
## map() aplica una función a CADA elemento de una lista.
## Aquí la usarás para calcular el precio con descuento de cada bebida.
## 1.- Usa map() con una lambda para multiplicar cada precio por 0.90
##    (que equivale a quitarle el 10%).
##    Estructura: map(lambda precio: precio * 0.90, orden)
## 2.- Convierte el resultado en lista con list() y guárdalo en
##    la variable precios_con_descuento.
## 3.- Imprime precios_con_descuento.
## Usal filter(): Filtrar solo las bebidas caras (más de $25)
##----------------------------------------------------------------
## filter() recorre una lista y se queda SOLO con los elementos
## que cumplen una condición (cuando la lambda devuelve True).
## 4.- Usa filter() con una lambda para quedarte solo con los precios
##    de precios_con_descuento que sean mayores a 25.
##    Estructura: filter(lambda precio: precio > 25, precios_con_descuento)
## 5.- Convierte el resultado en lista con list() y guárdalo en
##     la variable bebidas_caras.
## 6.- Imprime bebidas_caras.
## Usa reduce(): Calcular el total a pagar
##----------------------------------------------------------------
## reduce() combina todos los elementos de una lista en UN solo valor,
## aplicando la misma operación de izquierda a derecha.
## Para usarla primero hay que importarla:
##     from functools import reduce
## 7.- Importa reduce desde functools.
## 8.- Usa reduce() con una lambda que sume dos valores (acumulador + precio)
##    sobre la lista bebidas_caras.
##    Estructura: reduce(lambda acumulado, precio: acumulado + precio, bebidas_caras)
## 9.- Guarda el resultado en la variable total y luego imprímelo
##    con formato de 2 decimales.

from functools import reduce

# Lista de órdenes (precios)
orden = [25.50, 22.00, 35.75, 40.00, 18.50]

# Descuento del 10%
precios_con_descuento = list(
    map(lambda precio: precio * 0.90, orden)
)

print("\nPrecios con descuento:")
print(precios_con_descuento)

# Bebidas caras (>25)
bebidas_caras = list(
    filter(lambda precio: precio > 25, precios_con_descuento)
)

print("\nBebidas caras:")
print(bebidas_caras)

# Total
total = reduce(
    lambda acumulado, precio: acumulado + precio,
    bebidas_caras
)

print(f"\nTotal a pagar: ${total:.2f}")