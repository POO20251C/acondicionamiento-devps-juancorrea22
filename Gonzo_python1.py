# Clase 5/02/2025
# Problema número 1
# Juan Andres Correa Arenas
a=True
while a:
    try:
        numero=list(str(int(input('Ingrese un número entero: '))))
        a=False
    except ValueError:
        print('Ha sucedido un error. Por favor ingrese un número entero.')
        a=True

resultado=0
for i in range (len(numero)):
    resultado+=int(numero[i])

print(resultado)