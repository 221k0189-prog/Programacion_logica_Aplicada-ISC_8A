# Función que prepara una taza de café
def preparar_cafe():
    return "cafe"

# Función para tomar la orden
def ordenar_cafe(numero_tazas):
    tazas_cafe = [preparar_cafe() for _ in range(numero_tazas)]
    return tazas_cafe

# Número de tazas requeridas
cafe_para_grupo = ordenar_cafe(5)

# Imprimir el resultado
print(cafe_para_grupo)
                  