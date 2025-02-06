# Clase 5/02/2025
# Problema número 4
# Juan Andres Correa Arenas

ln=str(input('Ingrese una lista de números separada por espacios\n>: '))
nl=list(ln)[::-1]

for i in range(len(nl)):
    print(nl[i], end='')