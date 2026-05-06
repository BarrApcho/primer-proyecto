# Leer una matriz
def leer_matriz(m, n):
    matriz = []
    
    for i in range(m):
        fila = []
        for j in range(n):
            numero = int(input(f"Elemento [{i}][{j}]: "))
            fila.append(numero)
        matriz.append(fila)
    
    return matriz


# Encontrar el mayor valor
def mayor_valor(matriz):
    mayor = matriz[0][0]
    
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] > mayor:
                mayor = matriz[i][j]
    
    return mayor


# Imprimir matriz
def imprimir_matriz(matriz):
    print("\nMatriz ingresada:")
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            print(matriz[i][j], end=" ")
        print()


# Programa principal
m = int(input("Número de filas (m): "))
n = int(input("Número de columnas (n): "))

matriz = leer_matriz(m, n)

imprimir_matriz(matriz)

mayor = mayor_valor(matriz)

print("\nEl mayor valor de la matriz es:", mayor)