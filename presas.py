import random
class Presas :
    
    def __init__(self, simbolo: str = "🐟",  comida: int = 0):
        self.simbolo = simbolo
        self.comida = comida


    def agregar_peces_al_tablero(self,tablero, cantidad:int= 3 ):
        casillas_vacias_peces= tablero.buscar_celdas_vacias(tablero.matriz)

        if cantidad == 0 or not casillas_vacias_peces:
            return
        
        i,j = random.choice(casillas_vacias_peces)
        tablero.matriz[i][j] = self.simbolo
        return self.agregar_peces_al_tablero(tablero, cantidad -1)
        

    def movimiento_peces(self,tablero, x: int, y:int,   intentos = 3 ):

        if intentos == 0:
            return 

 
        casillas_con_plantas= tablero.obtener_celdas_adyacentes(self.x,self.y, "🌿")
        if casillas_con_plantas:
            nuevo_x, nuevo_y = random.choice(casillas_con_plantas)
            self.comida += 1
            tablero.matriz [nuevo_x][nuevo_y] = self.simbolo
            tablero.matriz [x] [y] = "__"
            self.x, self.y = nuevo_x, nuevo_y
            return
        
        casilla_libre = tablero.obtener_celdas_adyacentes(self.x, self.y , "__")
        if casilla_libre:
            nuevo_x, nuevo_y = random.choice(casilla_libre)
            tablero.matriz [self.x] [self.y] = "__"
            self.x, self.y = nuevo_x, nuevo_y
            tablero.matriz [nuevo_x][nuevo_y] = self.simbolo
            return
        

        if self.comida == 3:
            return self.reproducirse(tablero)
        
        return self.movimiento_peces(tablero,x, y ,  intentos - 1)
    
        

    def reproducirse( self, tablero):

        casillas_libres= tablero.obtener_celdas_adyacentes("__")

        if self.comida < 3 or not casillas_libres:
            return 
        
        
        nuevo_i, nuevo_j = random.choice(casillas_libres)
        nuevo_pez= Presas(nuevo_i, nuevo_j)
        tablero.matriz[nuevo_i][nuevo_j]= nuevo_pez.simbolo
        tablero.presas.append(nuevo_pez)
        self.comida = 0
        return self.reproducirse(tablero)
        

