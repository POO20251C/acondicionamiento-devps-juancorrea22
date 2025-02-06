# Clase 5/02/2025
# Problema número 5
# Juan Andres Correa Arenas

ln=(str(input('Ingrese una lista de números separada por espacios\n>: '))).split(' ')

a=0
for i in range(len(ln)):
    if int(ln[i])>a:
        a=int(ln[i])

print(f'El mayor número de la lista es {a}.')