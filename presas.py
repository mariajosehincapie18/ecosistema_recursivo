class Presas :
    
    def __init__(self, simbolo: str = "🐟",  comida: int = 0):
        self.simbolo = simbolo
        self.comida = comida

    def movimiento_peces(self, tablero ):

        casillas_vacias_pre= tablero.buscar_celdas_vacias(tablero.matriz)

            