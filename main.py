from tablero import Tablero

tablero = Tablero()
matriz = tablero.generar_tablero(3)
tablero.agregar_platas_al_tablero(matriz)
tablero.agregar_pescados(matriz)
tablero.agregar_tiburones(matriz)
        
#aqui voy a ver si la matriz se llena(borrar al final)
for fila in matriz:
    print (fila)
