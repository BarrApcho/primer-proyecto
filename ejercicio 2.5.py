a=123
print(type(a))

i=7
if isinstance(i, int):
    i+=1
elif isinstance(i, str):
    i=int(i)
    i+=1
print(i)

x = None
if x is None:
 print('Not a surprise, I just defined x as None.')

a='123'
b=int(a)
print(type(b))


def f(m):
    m.append(3)   # agrega un número a la lista

x = [1, 2]
f(x)
print(x)   # [1, 2, 3]  ✅ cambió la lista original

def g(t):
    # no existe forma de modificar la tupla directamente
    pass

x = (1, 2)
g(x)
print(x)   # (1, 2) ✅ siempre será igual

names=['Alice', 'Bob', 'Charlie','Craig','Diana','Eric']
print(names[-4])

names[0]='Anna'
print(names)

names.append("Sia")
print(names)  
# ['Alice', 'Bob', 'Craig', 'Diana', 'Eric', 'Sia']

names.insert(1, "Nikki")
print(names)  
# ['Alice', 'Nikki', 'Bob', 'Craig', 'Diana', 'Eric', 'Sia']

names.remove("Bob")
print(names)  
# ['Alice', 'Nikki', 'Craig', 'Diana', 'Eric', 'Sia']

names = ['Alice', 'Bob', 'Craig', 'Diana', 'Eric', 'Sia']
print(names.index("Alice"))   # 0
print(names.index("Craig"))   # 2

print(len(names))   # 6

a = [1, 1, 1, 2, 3, 4]
print(a.count(1))   # 3

a.reverse()
print(a)   # [4, 3, 2, 1, 1, 1]

print(a[::-1])

my_list = [10, 20, 30]
for element in my_list:
    print(element)
# 10
# 20
# 30

# Una tupla normal
ip_address = ('10.20.30.40', 8080)

# Tupla con un solo elemento
one_member_tuple = ('Only member',)
one_member_tuple2 = 'Only member',

# Acceso como en listas
print(ip_address[0])  # '10.20.30.40'
print(ip_address[1])  # 8080

state_capitals = {
    'Arkansas': 'Little Rock',
    'Colorado': 'Denver',
    'California': 'Sacramento',
    'Georgia': 'Atlanta'
}

# Acceder con la clave
print(state_capitals['California'])  # Sacramento

# Iterar sobre claves
for k in state_capitals.keys():
    print(f"{state_capitals[k]} is the capital of {k}")

# Crear un set directamente
first_names = {'Adam', 'Beth', 'Charlie'}

# Crear un set desde una lista
my_list = [1, 2, 3, 1, 2]
my_set = set(my_list)   # {1, 2, 3}

# Comprobar pertenencia
if 'Adam' in first_names:
    print("Adam está en el conjunto")

# Recorrer
for name in first_names:
    print(name)

from collections import defaultdict

# Diccionario con valor por defecto 'Boston'
state_capitals = defaultdict(lambda: 'Boston')

# Asignamos algunos valores
state_capitals['Arkansas'] = 'Little Rock'
state_capitals['California'] = 'Sacramento'

# Acceso normal
print(state_capitals['California'])  # Sacramento

# Acceso a una clave inexistente → devuelve el valor por defecto
print(state_capitals['Alabama'])     # Boston

name = input("What is your name? ")
print("Hello,", name)

x = input("Write a number: ")
x = int(x)      # convertir a entero
print(x / 2)

def saludar(nombre):
    return f"Hola, {nombre}"

print(saludar("Lucas"))  # Hola, Lucas