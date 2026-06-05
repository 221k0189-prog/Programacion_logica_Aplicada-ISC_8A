## Ejerccio 2: Ordenar tipo de cafe
# Objetivo : Ordenar distintos tipos de cafe

def preparar_cafe():
    return "cafe americano"

def preparar_cafe_olla():
    return "cafe de olla"

def ordenar_cafe(preparar_cafe, numero_tazas):
    tazas_cafe =[preparar_cafe() for _ in range(numero_tazas)]
    return tazas_cafe

cafe_grupo_A = ordenar_cafe(preparar_cafe, 4)

cafe_grupo_B = ordenar_cafe(preparar_cafe_olla, 3)

print(cafe_grupo_A, cafe_grupo_B)
