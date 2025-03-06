import random
class Presas :
    
    def __init__(self,   comida: int = 0):
        self.comida = comida


    def agregar_peces_al_tablero(self,tablero,simbolo: str = "🐟", cantidad:int= 3 ):
        return tablero.agregar_al_tablero(simbolo, cantidad)

        

    def movimiento_peces(self,tablero,    intentos = 3 ):

        if intentos == 0:
            return 

 
        casillas_con_plantas= tablero.obtener_celdas_adyacentes(self.x,self.y, "🌿")
        if casillas_con_plantas:
            nuevo_x, nuevo_y = random.choice(casillas_con_plantas)
            self.comida += 1
        
        else: 
            casilla_libre = tablero.obtener_celdas_adyacentes(self.x, self.y , "__")
            if casilla_libre:
                nuevo_x, nuevo_y = random.choice(casilla_libre)

            else:
                return self.movimiento_peces(tablero, intentos-1)
            
        tablero.matriz[self.x][self.y] ="__"
        self.x, self.y = nuevo_x, nuevo_y
        tablero.matriz[self.x][self.y] = self.simbolo

    

        if self.comida == 3:
            return self.reproducirse(tablero)
        
      
    
        

    def reproducirse( self, tablero):

        casillas_libres= tablero.obtener_celdas_adyacentes("__")
        if self.comida < 3 or not casillas_libres:
            return 
        
        
        nuevo_x, nuevo_y = random.choice(casillas_libres)
        tablero.presas.append(Presas(nuevo_x, nuevo_y))
        tablero.matriz[nuevo_x][nuevo_y]= self.simbolo
        self.comida = 0
        return self.reproducirse(tablero)
        

