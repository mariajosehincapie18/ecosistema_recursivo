from tablero import Tablero
from plantas import Plantas
from presas import Presas
from depredadores import Depredador
import time

def imprimir_tablero(matriz, i= 0):
    if i == len(matriz):
        print("\n"+"__"*(len(matriz)*3))
        return
    
    print(" ".join(matriz[i]))
    return imprimir_tablero(matriz, i +1)


def simulacion(tablero, plantas, presas, depredadores, ciclos):
    if ciclos == 0:
       return

    print(f"ciclo{ciclos}") 

    mover_presa(tablero, presas, 0)
    mover_depredadores(tablero, depredadores, 0)
  

    imprimir_tablero(tablero.matriz)
    time.sleep(1)

    return simulacion(tablero, plantas, presas, depredadores, ciclos -1)
   
def mover_presa(tablero, presas, index: int):
    if index == len(presas):
        return
    presas[index].movimiento_peces(tablero)

    return mover_presa(tablero, presas, index + 1)

def mover_depredadores(tablero, depredadores, index: int):
    if index ==len(depredadores):
        return
    depredadores[index].mover_tiburones(tablero)
    
    return mover_depredadores(tablero, depredadores, index +1)



def inicializar(cls, cantidad:int, lista= None):
    if lista is None:
        lista = []
    if cantidad == 0:
        return lista 
    
    return inicializar(cls, cantidad -1, lista + [cls(cantidad)])



def agregar_entidades(entidades, tablero, index= 0):
    if index == len(entidades):
        return
    
    if isinstance(entidades[index], Presas):
        entidades[index].agregar_peces_al_tablero(tablero)
    elif isinstance(entidades[index], Depredador):
        entidades[index].agregar_tiburones(tablero)
    agregar_entidades(entidades, tablero, index + 1)

tablero= Tablero(5)
plantas= Plantas(2)
plantas.crecer(tablero)
presas = inicializar(Presas, 2)
depredadores= inicializar(Depredador, 2)

agregar_entidades(presas, tablero)
agregar_entidades(depredadores, tablero)

simulacion(tablero, presas, depredadores, plantas, 5)

