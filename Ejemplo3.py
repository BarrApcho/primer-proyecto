l1=float(input("Ingrese la longitud del lado 1: "))
l2=float(input("Ingrese la longitud del lado 2: "))
l3=float(input("Ingrese la longitud del lado 3: "))
perimetro=l1+l2+l3
sp=perimetro/2
area=(sp*(sp-l1)*(sp-l2)*(sp-l3))**(1/2)
print("El area del triangulo es: ",area)