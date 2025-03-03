from tablero import Tablero
from plantas import Plantas

tablero = Tablero(3)
planta = Plantas()
planta.crecer(tablero)




        
#aqui voy a ver si la matriz se llena(borrar al final)
for fila in tablero.matriz:
    print (fila)
