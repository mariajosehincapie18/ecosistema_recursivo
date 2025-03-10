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
    
    def buscar_celdas_vacias(self,matriz, i:int =0,  j:int= 0,  celdas_vacias:list=[]):
        if i == len(matriz):
            return celdas_vacias
        
        if j == len(matriz[0]):
            return self.buscar_celdas_vacias(matriz, i +1, 0, celdas_vacias)
        
        if  matriz [i][j] == "__":
            celdas_vacias.append((i, j))
        
        return self.buscar_celdas_vacias(matriz, i, j+1, celdas_vacias)
        
    
    def agregar_al_tablero(self, simbolo:str, cantidad: int):

        celdas_vacias= self.buscar_celdas_vacias(self.matriz)

        if  cantidad == 0 or not celdas_vacias:
            return 
        
        i, j= random.choice(celdas_vacias)
        self.matriz [i] [j] = simbolo
        return self.agregar_al_tablero(simbolo, cantidad -1)
    
    def obtener_celdas_adyacentes(self,i, j,  index =0,  adyacentes= []):
       
        movimientos = ((-1,0), (1,0), (0,-1), (0, 1) )
        if index == len(movimientos): 
            return adyacentes
        
        di, dj =movimientos [index]
        ni, nj = i + di, j + dj

        if 0 <= ni < len(self.matriz) and 0 <= nj < len(self.matriz[0]) and self.matriz [ni][nj] == "__":
            adyacentes.append((ni,  nj))

        return self.obtener_celdas_adyacentes( i, j,  index +1, adyacentes)
       
    def filtrar_plantas(self,  celdas, index= 0, casillas_con_plantas= []):
        if index == len(celdas):
            return casillas_con_plantas
        
        i, j =celdas[index]
        if self.matriz [i] [j] == "🌿":
            casillas_con_plantas.append((i,j))


        return self.filtrar_plantas(celdas, index+1, casillas_con_plantas)


    
    def filtrar_casillas(self, celdas, index= 0, casillas_vacias= []):
        if index == len(celdas):
            return casillas_vacias
        
        i, j =celdas[index]
        if self.matriz [i] [j] == "__":
            casillas_vacias.append((i,j))

        return self.filtrar_plantas(celdas, index+1, casillas_vacias)
    
    def filtrar_presa_cercana(self, celdas, index= 0, casilla_con_presa= []):
        if index == len(celdas):
            return casilla_con_presa
        
        i,j = celdas[index]
        if self.matriz [i][j] == "🐟":
            casilla_con_presa.append((i,j))

        return self.filtrar_presa_cercana( celdas, index +1, casilla_con_presa)
        
        
       
       
        










