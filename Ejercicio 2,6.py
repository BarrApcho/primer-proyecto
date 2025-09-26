import math
print(dir(math))

"""Este es el docstring del módulo."""

def saludar():
    """Este es el docstring de la función."""
    return "Hola Mundo"
print(saludar())

class MiClase:
    """Docstring de mi clase"""
    pass

print(dir(MiClase))

print(str(123))     # "123"
print(str(3.14))    # "3.14"
print(str(True))    # "True"

# hello.py
def say_hello():
    print("Hello!")
