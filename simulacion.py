from tablero import Tablero
from plantas import Plantas
from presas import Presas
from depredadores import Depredador
import time

def imprimir_tablero(tablero, index= 0):
    if index == len(tablero.matriz):
        print("\n"+ "__" * 40 + "\n")
        return
    print(" ".join(tablero.matriz[index]))
    imprimir_tablero(tablero, index +1)

def simulacion(tablero, plantas, presas, depredadores, iteraciones):
    if iteraciones == 0:
       return

    print(f"Iteracion{iteraciones}") 
    plantas.crecer(tablero)

    def mover_entidades( entidades, metodo, index = 0):
        if index == len(entidades):
           return
       
        getattr(entidades[index], metodo)(tablero)
        mover_entidades(entidades, metodo, index + 1)
    
    mover_entidades(presas, "movimiento_peces")
    mover_entidades(depredadores, "mover_tiburones")

    imprimir_tablero(tablero)
    time.sleep(1)
    simulacion(tablero, plantas, presas, depredadores, iteraciones -1 )
   
def crear_entidades (cls,n, entidades= None):
    if n == 0:
        return [] if entidades is None else entidades
    return crear_entidades(cls, n -1, (entidades or[]) + [cls()])

tablero = Tablero(4)
plantas= Plantas()
presas= crear_entidades(Presas, 1)
depredadores= crear_entidades(Depredador, 1)


def  agregar_entidades(entidades, metodo, index= 0):
    if index == len(entidades):
        return
    getattr(entidades[index], metodo)(tablero)
    agregar_entidades(entidades, metodo, index +1)
plantas.crecer(tablero)
agregar_entidades(presas, "agregar_peces_al_tablero")
agregar_entidades(depredadores, "agregar_tiburones")


simulacion(tablero, plantas, presas, depredadores, 5)


