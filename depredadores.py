import random
class Depredador :
    
    def __init__(self, i:int = 0, j: int= 0,   energia: int= 50 ):
        self.energia = energia
        self.i = i
        self.j = j
        self.simbolo = "🦈"
    
    def  agregar_tiburones(self, tablero,  cantidad: int = 1):
      return tablero.agregar_al_tablero(self.simbolo, cantidad)
    
    def mover_tiburones(self, tablero, intentos = 3):
        if intentos == 0:
            return
        
        casillas_adyacentes = tablero.obtener_celdas_adyacentes(self.i, self.j)
        casilla_con_presa = tablero.filtrar_presa_cercana(casillas_adyacentes)
        
        if casilla_con_presa:
            nuevo_i, nuevo_j = random.choice(casilla_con_presa)
            self.energia += 2
        
        else:
            casilla_libre = tablero.filtrar_casillas(casillas_adyacentes)
            if casilla_libre:
                nuevo_i, nuevo_j = random.choice(casilla_libre)
            else:
                return self.mover_tiburones(tablero, intentos-1)
       
        tablero.matriz[self.i][self.j] ="__"
        self.i, self.j = nuevo_i, nuevo_j
        tablero.matriz[self.i][self.j] = self.simbolo

        if self.energia >= 6:
            return self.reproducirse(tablero)

    def reproducirse(self, tablero):

        casillas_libres = tablero.obtener_celdas_adyacentes(self.i, self.j)

        if self.energia < 6 or not casillas_libres:
            return
        
        nuevo_i, nuevo_j = random.choice(casillas_libres)
        tablero.matriz[nuevo_i][nuevo_j]= self.simbolo
        self.energia = 0
        
        
            
        

        
            
       
        
 
