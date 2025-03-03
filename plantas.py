import random
class Plantas () :
    
    def __init__(self,  simbolo:str ="🌿" ):
        self.simbolo = simbolo

    def crecer(self, tablero, cantidad: int = 4 ):
        
        casillas_vaciaspl = tablero.buscar_celdas_vacias(tablero.matriz)

        if cantidad == 0 or not casillas_vaciaspl: 
            print("no hay casillas disponibles para las plantas")
            return
        
        i,j = random.choice(casillas_vaciaspl)
        tablero.matriz[i][j] = self.simbolo
        return self.crecer(tablero, cantidad -1)
        

    

    
   