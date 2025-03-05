
class depredador :
    
    def __init__(self, energia: int= 50 ):
        self.energia = energia
    
    def  agregar_tiburones(self, tablero,simbolo:str ="🦈",  cantidad: int = 2):
        return tablero.agregar_al_tablero(simbolo, cantidad)
        
            
       
        
 
