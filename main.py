from tablero import Tablero

tablero = Tablero()
matriz = tablero.generar_tablero(5)
        
#aqui voy a ver si la matriz se llena(borrar al final)
for fila in matriz:
    print (fila)
