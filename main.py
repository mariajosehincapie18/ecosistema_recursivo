from tablero import Tablero
from plantas import Plantas
from presas import Presas
from depredadores import Depredador
import time
def simulacion(tablero, plantas, presas, depredadores, iteraciones):
    if iteraciones == 0:
       return

    print(f"Iteracion{iteraciones}")
tablero = Tablero(4)
planta = Plantas()
planta.crecer(tablero)
presa = Presas()
presa.agregar_peces_al_tablero(tablero)
tiburon = Depredador()
tiburon.agregar_tiburones(tablero)
for fila in tablero.matriz:
    print (fila)

presa.movimiento_peces(tablero)
presa.reproducirse(tablero)
tiburon.mover_tiburones(tablero)
tiburon.reproducirse(tablero)






