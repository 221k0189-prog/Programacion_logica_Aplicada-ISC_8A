## Evaluación Tema 2


## Ejercicio 1: PRESETANCIÓN PERSONAL

nombre = "Carlos"                   
edad = 24                         
ciudad = "Chetumal"  
es_estudiante = True              

print("Mi nombre es:", nombre)  
print("Mi edad es:", edad)      
print("Vivo en:", ciudad)      
print("¿Soy de ISC?", es_estudiante) 


print("Hola, me llamo " + nombre + ", tengo " + str(edad) + " años, vivo en " + ciudad + " y soy ISC.")

## Ejercicio 2: CASA DE CAMBIO



## Ejercicio 3: ¿QUIEN ES MAYOR DE EDAD?

nombre1 = input("Nombre de la primera persona: ")
edad1 = int(input("Edad de " + nombre1 + ": "))

nombre2 = input("Nombre de la primera persona: ")
edad2 = int(input("Edad de " + nombre1 + ": "))

if edad1 > edad2:
    diferencia = edad1 - edad2
    print(nombre1, "es mayor que", nombre2, "por", diferencia, "años.")
else:
    diferencia = edad2 - edad1
    print(nombre2, "es mayor que", nombre1, "por", diferencia, "años.")
