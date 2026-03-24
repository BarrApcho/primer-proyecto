##Determine  a+b+c la siquiente adiccon :##
##2+23+232+2323+.......+232332323232....232(como 23 cifras)=...abc##
n = 23  # Número de cifras
def calcular_suma(n):
    if n == 0:
        return 0
    num = 2
    suma = 2
    for i in range(2, n + 1):
        if i % 2 == 0:
            num = num * 10 + 3
        else:
            num = num * 10 + 2
        suma += num
    return suma

resultado = calcular_suma(n)
print("El resultado de la suma es:", resultado)

# Calcular a+b+c donde abc son los últimos tres dígitos
ultimos_tres = resultado % 1000
a = ultimos_tres // 100
b = (ultimos_tres // 10) % 10
c = ultimos_tres % 10
suma_digitos = a + b + c
print("Los últimos tres dígitos son:", ultimos_tres)
print("a + b + c =", suma_digitos)