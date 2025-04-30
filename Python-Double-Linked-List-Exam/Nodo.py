"""
+=========================================== +
| AUTOR: ALEX DIAZ y SSLER FLORES            |
| FECHA: 25-04-2025                          |
| DESCRIPCIÓN: Esta es la definición de      |
| la clase nodo, que es la base de la        |
| lista doblemente enlazada.                 |
| VERSION: 1.0                               |
+=========================================== +
"""
# crear el nodo de una lista doublemente enlazada
class Node:
    def __init__(self, action, type_of_action):
        self.action = action
        self.type_of_action = type_of_action
        self.next = None
        self.prev = None
