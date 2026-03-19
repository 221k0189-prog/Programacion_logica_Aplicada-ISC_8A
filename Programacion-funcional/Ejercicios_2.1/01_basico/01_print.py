from os import system

if system("clear") != 0: system("cls")

#este es un ejemplo basico de como imprimir un texto en consola
print("¡Hola, Crayola!")

#tambien puedes usar comillas simples 
print('Esto también funciona con una comilla')

#puedes imprimir multiples elementos por un espacio 
print("Python", "es", "genial")

# el parametro 'sep' permite definir como se seperan los elementos impresos
print("Python", "es", "brutal", sep = "-")

# el parametro 'end' define lo que se va imprimir al final de la linea
print("ESto se imprime", end = "\n") # aqui, el 'end' tiene un salto de linea
print("en una linea") # esto se imprime en lines siguiente

#tambien se puede imprimir numeros directamente
print(42)

# ejemplo de como imprimir el simbolo de pulgada ('')
#si usamos comillas dobles dentro de un string con comillas dobles
#print("Este es una pulgada") # esto genera un error

# solucion 1: usar comillas simples para encerrar la cadena
print('esto es una "pulgada" dentro de un string con comillas simples')

# solucion 2:
print("esto es una \"pulgada\" dentro de un string con comillas dobles")

#solucion 3 
print("Esto es una \"pulgada\" dentro de un string con comillas Triples")