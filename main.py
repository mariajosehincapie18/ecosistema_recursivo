from tablero import Tablero
from plantas import Plantas
from presas import Presas
from depredadores import Depredador
 
tablero = Tablero(8)
planta = Plantas()
planta.crecer(tablero)
presa = Presas()
presa.agregar_peces_al_tablero(tablero)
tiburon = Depredador()
tiburon.agregar_tiburones(tablero)
presa.movimiento_peces(tablero)
presa.reproducirse(tablero)
tiburon.mover_tiburones(tablero)
tiburon.reproducirse(tablero)
for fila in tablero.matriz:
    print (fila)








        
#aqui voy a ver si la matriz se llena(borrar al final)
for fila in tablero.matriz:
    print (fila)
