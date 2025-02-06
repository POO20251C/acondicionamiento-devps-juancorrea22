# Clase 5/02/2025
# Problema número 3
# Juan Andres Correa Arenas

texto = str(input('Ingrese un palindromo: ')).lower()

for i in ' ':
    texto=texto.replace(i, '')

if list(texto) == list(texto)[::-1]:
    print(f'{texto} si es un palindromo.')
    
elif list(texto) != list(texto)[::-1]:
    print(f'{texto} no es un palindromo.')