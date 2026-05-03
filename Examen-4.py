# precios de las camisas
precio_antonios = 30.5
precio_rodrich = 28.9
precio_luiggi = 35.4

def mostrar_menu():
    print("\nMARCAS DE CAMISAS")
    print("1. Antonios")
    print("2. Rodrich")
    print("3. Luiggi")

def obtener_precio(marca):

    if marca == 1:
        return precio_antonios
    elif marca == 2:
        return precio_rodrich
    elif marca == 3:
        return precio_luiggi

def calcular_descuento(compra, cantidad):

    if 1 <= cantidad <= 3:
        return compra * 0.04
    elif cantidad <= 5:
        return compra * 0.065
    else:
        return compra * 0.09

def mostrar_resultado(compra, descuento, pagar):

    print("Importe de compra:", compra)
    print("Descuento:", descuento)
    print("Total a pagar:", pagar)

def tienda_camisas():

    camisas_a = camisas_r = camisas_l = 0
    importe_a = importe_r = importe_l = 0

    seguir = "s"

    while seguir.lower() == "s":

        mostrar_menu()

        marca = int(input("Seleccione marca: "))
        cantidad = int(input("Cantidad de camisas: "))

        precio = obtener_precio(marca)

        compra = precio * cantidad
        descuento = calcular_descuento(compra, cantidad)
        pagar = compra - descuento

        mostrar_resultado(compra, descuento, pagar)

        if marca == 1:
            camisas_a += cantidad
            importe_a += pagar
        elif marca == 2:
            camisas_r += cantidad
            importe_r += pagar
        else:
            camisas_l += cantidad
            importe_l += pagar

        seguir = input("Otra venta? (s/n): ")

    print("\n--- RESUMEN DE VENTAS ---")
    print("Antonios -> Camisas:", camisas_a, "Importe:", importe_a)
    print("Rodrich -> Camisas:", camisas_r, "Importe:", importe_r)
    print("Luiggi -> Camisas:", camisas_l, "Importe:", importe_l)

# ejecutar programa
tienda_camisas()