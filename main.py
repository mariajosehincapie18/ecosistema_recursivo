from tablero import Tablero
from plantas import Plantas
from presas import Presas
from depredadores import depredador
 
tablero = Tablero(8)
planta = Plantas()
planta.crecer(tablero)
presa = Presas()
presa.agregar_peces_al_tablero(tablero)
tiburon = depredador()
tiburon.agregar_tiburones(tablero)
presa.movimiento_peces(tablero)
for fila in tablero.matriz:
    print (fila)








        
#aqui voy a ver si la matriz se llena(borrar al final)
for fila in tablero.matriz:
    print (fila)
