# ecosistema_recursivo
practica 1 de estructuras (recursion)
Simulación de Ecosistema Recursivo

Objetivo:
El objetivo de esta práctica es desarrollar un ecosistema simulado donde diferentes tipos de organismos interactúan entre sí de manera estrictamente recursiva. La solución debe modelar el comportamiento de depredadores, presas y recursos dentro de un entorno definido, asegurando que todas las operaciones de actualización y evaluación del ecosistema sean implementadas usando recursión exclusivamente.

Descripción de la Actividad:
Los estudiantes deben trabajar en parejas para diseñar e implementar un sistema recursivo que simule la evolución de un ecosistema. La simulación se ejecutará en ciclos donde los organismos interactúan según reglas predefinidas y sus estados cambian en cada iteración.

Elementos del Ecosistema:
El ecosistema se representará en una matriz NxN, donde cada celda puede contener un organismo o estar vacía. Existen tres tipos de entidades principales:
* Depredadores (ejemplo: lobos)
Cazan presas en celdas adyacentes.
Mueren si no se alimentan en un número determinado de ciclos.
Pueden reproducirse si alcanzan cierta cantidad de energía (Opcional).
Se mueven a una celda vacía adyacente siguiendo la regla de menor distancia a una presa visible.
Las presas visibles son las presas que se ubican en su misma fila o misma columna. Si no tiene ninguna, se moverá un espacio de manera aleatoria en cualquier dirección ortogonal.
* Presas (ejemplo: conejos)
Se mueven buscando alimento (plantas o hierba) en celdas adyacentes.
Son cazadas por depredadores si comparten una celda.
Se reproducen si hay suficiente comida disponible.
se tienen que reprodcir cuando se junta con otras presas
Su movimiento es aleatorio entre las celdas vacías disponibles en su entorno inmediato.
*Plantas 
Son consumidas por las presas.
Se regeneran cada cierto número de ciclos en celdas vacías seleccionadas aleatoriamente.


Reglas de la Simulación:
En cada ciclo, se debe evaluar el estado de todos los organismos en la matriz.
La interacción entre organismos (caza, reproducción, muerte) debe resolverse de manera recursiva.
Los movimientos deben realizarse evaluando recursivamente las opciones disponibles.

La simulación termina cuando:
No quedan organismos vivos.
Se alcanza un número límite de ciclos.

Restricciones Importantes:
Toda la lógica del programa debe implementarse con recursión. No se permiten estructuras iterativas (for, while).
La simulación debe funcionar de manera determinista, garantizando que los organismos sigan reglas claras en cada ciclo.
El código debe estar correctamente estructurado para facilitar su lectura y corrección.
Evite comentar el código para la entrega. 

Entrega y Evaluación:
Formato de Entrega
Repositorio con el código fuente.


