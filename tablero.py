class Tablero:
    def generar_tablero(self, n: int, i:int = 0 , j: int = 0, fila :list[str] = [], matriz:list[list[str]] = [], ) -> list[list[str]]:
        if(i == n):
             return matriz
        if (j == n):
            matriz.append(fila)
            return self.generar_tablero(n, i +1, 0, [], matriz )
        
        fila.append("__")
        return self.generar_tablero(n, i, j+1, fila, matriz)


class posiciones:
    def __init__(self, x,y ):
        self.x = x
        self.y= y



