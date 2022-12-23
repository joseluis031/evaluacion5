from gestor import *
if __name__ == "__main__":
    
    a = Personajes("Guerrero", 100, 90, 77, 11)
    b = Personajes("Arquero", 50, 10, 50, 90)
    c = Personajes("Caballero", 80, 70, 9, 33)

    d = Gestor()
    d.agregar(a)
    d.agregar(b)
    d.agregar(c)
    
    d.mostrar()
    
    d.eliminar("Caballero")