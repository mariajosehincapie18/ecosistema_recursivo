from plantas import Plantas
import random
class Tablero:
    def generar_tablero(self, n: int, i:int = 0 , j: int = 0, fila :list[str] = [], matriz:list[list[str]] = [], ) -> list[list[str]]:
        if(i == n):
             return matriz
        if (j == n):
            matriz.append(fila)
            return self.generar_tablero(n, i +1, 0, [], matriz )
        
        fila.append("__")
        return self.generar_tablero(n, i, j+1, fila, matriz)
    

    def agregar_platas_al_tablero(self, matriz):
        self.matriz = matriz

        celdas_vacias= [(i,j)for i in range (len(matriz)) for j in range(len(matriz[0])) if matriz [i][j] == "__"] 

        if celdas_vacias:
            i, j= random.choice(celdas_vacias)
            matriz [i][j] = "Pl"







