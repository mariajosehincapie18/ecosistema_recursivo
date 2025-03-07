import random
class Presas :
    
    def __init__(self,   comida: int = 0, i:int = 0, j:int = 0):
        self.comida = comida
        self.i= i
        self.j = j
        self.simbolo = "🐟"


    def agregar_peces_al_tablero(self,tablero, cantidad:int= 0):
        return tablero.agregar_al_tablero(self.simbolo, cantidad) 


    def movimiento_peces(self,tablero, intentos = 3 ):

        if intentos == 0:
            return 

        casillas_adyacentes= tablero.obtener_celdas_adyacentes(self.i , self.j)
        casillas_con_plantas= tablero.filtrar_plantas(casillas_adyacentes)

        if casillas_con_plantas:
            nuevo_i, nuevo_j = random.choice(casillas_con_plantas)
            self.comida += 1
        
        else: 
            casilla_libre = tablero.filtrar_casillas(casillas_adyacentes)
            if casilla_libre:
                nuevo_i, nuevo_j = random.choice(casilla_libre)

            else:
                return self.movimiento_peces(tablero, intentos -1)
            
        tablero.matriz[self.i][self.j] ="__"
        self.i, self.j = nuevo_i, nuevo_j
        tablero.matriz[self.i][self.j] = self.simbolo

    

        if self.comida == 3:
            return self.reproducirse(tablero)
           
        

    def reproducirse( self, tablero):

        casillas_libres= tablero.obtener_celdas_adyacentes(self.i, self.j)
        if self.comida < 3 or not casillas_libres:
            return 
        
        
        nuevo_i, nuevo_j = random.choice(casillas_libres)
        tablero.matriz[nuevo_i][nuevo_j]= self.simbolo
        self.comida = 0
        
        

