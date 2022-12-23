import pickle
import os

class Personajes:
    
    def __init__(self, nombre, vida, ataque, defensa, alcance):
        self.nombre = nombre
        self.vida = vida
        self.ataque = ataque
        self.defensa = defensa
        self.alcance = alcance
        
    def __str__(self):
        return f"Nombre: {self.nombre} Vida: {self.vida} Ataque: {self.ataque} Defensa: {self.defensa} Alcance: {self.alcance}"
    
class Gestor:
    def __init__(self):
        self.personajes = []
    
    def agregar(self, personaje):
        self.personajes.append(personaje)
        
    def eliminar(self, nombre):
        for personaje in self.personajes:
            if personaje.nombre == nombre:
                self.personajes.remove(personaje)
                print("Personaje eliminado")
                break
        else:
            print("No existe el personaje")
            
    def mostrar(self):
        for personaje in self.personajes:
            print(personaje)

    
    def cargar(self):
        if os.path.exists("personajes.pckl"):
            fichero = open("personajes.pckl", "rb")
            self.personajes = pickle.load(fichero)
            fichero.close()
        else:
            print("No existe el fichero")
    
    def guardar(self):
        fichero = open("personajes.pckl", "wb")
        pickle.dump(self.personajes, fichero)
        fichero.close()
        
