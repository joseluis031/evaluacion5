import pickle
import os

def crear_fichero():
    try:
        f = open("contador.txt", "r")
        f.close()
    except:
        f = open("contador.txt", "w")
        f.write("0")
        f.close()
        
def leer_fichero():
    f = open("contador.txt", "r")
    leer = f.read()
    f.close()
    return leer

def escribir_fichero(argumento):
    if argumento == "inc":
        contador = leer_fichero()
        contador += 1
        f = open("contador.txt", "w")
        f.write(str(argumento))
        f.close()
        print("EL fichero tiene: {}".format(contador))
    elif argumento == "dec":
        contador = leer_fichero()
        contador -= 1
        f = open("contador.txt", "w")
        f.write(str(argumento))
        f.close()
        print("EL fichero tiene: {}".format(contador))
    else:
        print("EL fichero tiene: {}".format(contador))


escribir_fichero("inc")

    
 