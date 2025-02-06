# Clase 5/02/2025
# Problema número 2
# Juan Andres Correa Arenas
vocales={'a','e','i','o','u'}

texto=list((str(input('Ingrese su texto: '))).lower())
contador=0
for i in range (len(texto)):
    if texto[i] in vocales:
        contador+=1

print(contador)