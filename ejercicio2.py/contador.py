

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
    contador = (f.read())
    f.close()
    return contador

def escribir_fichero(argumento):
    if argumento == "inc":
        contador = leer_fichero()
        contador = int(contador) + 1  
        f = open("contador.txt", "w")
        f.write(str(contador))
        f.close()
        print("EL contador tiene: {}".format(contador))
    elif argumento == "dec":
        contador = leer_fichero()
        contador = int(contador) - 1
        f = open("contador.txt", "w")
        f.write(str(contador))
        f.close()
        print("EL contador tiene: {}".format(contador))
    else:
        print("EL contador tiene: {}".format(contador))


