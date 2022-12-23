def suma(a,b):
    try:
        a = int(a)
        b = int(b)
        return a + b
    except ValueError:
        print("Introduzca un numero entero")

def resta(a,b):
    try:
        a = int(a)
        b = int(b)
        return a - b
    except ValueError:  
        print("Introduzca un numero entero")

def producto(a,b):
    try:
        a = int(a)
        b = int(b)
        return a * b
    except ValueError:
        print("Introduzca un numero entero")
    

def division(a,b):
    try:
        a = int(a)
        b = int(b)
        return a / b
    except ValueError:
        print("Introduzca un numero entero")
    except ZeroDivisionError:
        print("No se puede dividir entre 0")