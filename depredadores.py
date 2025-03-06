import random
class depredador :
    
    def __init__(self, energia: int= 50 ):
        self.energia = energia
    
    def  agregar_tiburones(self, tablero,simbolo:str ="🦈",  cantidad: int = 2):
        return tablero.agregar_al_tablero(simbolo, cantidad)
    
    def mover_tiburones(self, tablero, intentos = 3):
        if self.energia == 0:
            tablero.matriz[self.x][self.y] = "__"
            tablero.depredador.remove(self)
            return
        
        presas_cercana= tablero.obtener_celdas_adyacetes(self.x, self.y, "🐟")
        if presas_cercana:
            nuevo_x, nuevo_Y = random.choice(presas_cercana)
            self.energia +=2

        else:
            casilla_libred = tablero.btener_celdas_adyacentes(self.x, self.y, "__")
            if casilla_libred:
                nuevo_x, nuevo_Y = random.choice(casilla_libred)

            else:
                return self.mover_tiburones(tablero, intentos -1)
        
        
        tablero.matriz[self.x][self.y] ="__"
        self.x, self.y = nuevo_x, nuevo_Y
        tablero.matriz[self.x][self.y] = self.simbolo

        if self.energia >= 6:
            return self.reproducirse(tablero)

    def reproducirse(self, tablero):

        casillas_libres = tablero.obtener_celdas_adyacentes("__")

        if self.energia < 6 or not casillas_libres:
            return
        
        nuevo_x, nuevo_y = random.choice(casillas_libres)
        tablero.depredador.append(depredador(nuevo_x, nuevo_y))
        tablero.matriz[nuevo_x][nuevo_y]= self.simbolo
        self.energia = 0
        return self.reproducirse(tablero)
        
            
        

        
            
       
        
 
