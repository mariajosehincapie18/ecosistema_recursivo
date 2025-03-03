from plantas import Plantas
import random
class Tablero:
     
    def __init__(self, n: int):
        self.n = n
        self.matriz = self.generar_tablero(n)
            
    def generar_tablero(self, n: int, i:int = 0 , j: int = 0, fila :list[str] = [], matriz:list[list[str]] = [], ) -> list[list[str]]:
        if(i == n):
             return matriz
        if (j == n):
            matriz.append(fila[:])
            return self.generar_tablero(n, i +1, 0, [], matriz )
        
        fila.append("__")
        return self.generar_tablero(n, i, j+1, fila, matriz)
    
    def buscar_celdas_vacias(self, matriz):
        return [(i,j)for i in range (len(matriz)) for j in range(len(matriz[0])) if matriz [i][j] == "__"] 
    
    def agregar_al_tablero(self, simbolo:str, cantidad: int):

        celdas_vacias= self.buscar_celdas_vacias()

        if  cantidad == 0 or not celdas_vacias:
            return 
        
        i, j= random.choice(celdas_vacias)
        self.matriz [i] [j] = simbolo
        return self.agregar_al_tablero(simbolo, cantidad -1)
    
    def obtener_celdas_adyacentes(self, tablero, index =0, adyacentes = []):
        movimientos = ((-1,0), (1,0), (0,-1), (0, 1) )
        if index == len(movimientos):
            return adyacentes
        
        di, dj =movimientos [index]
        ni, nj = self.i + di, self.j + dj

        if 0<= ni < len(tablero.matriz) and 0 <= nj < len(tablero.matriz[0]) and tablero.matriz [ni][nj] == "__":
            adyacentes.append((ni, nj))

        return self.obtener_celdas_adyacentes(tablero, index +1, adyacentes)
       
       
        










