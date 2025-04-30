"""
+=========================================== +
| AUTOR: ALEX DIAZ y SSLER FLORES            |
| FECHA: 25-04-2025                          |
| DESCRIPCIÓN: Esta es la definición de      |
| la clase ActionHistory, que es la lista    |
| doblemente enlazada.                       |
| VERSION: 1.0                               |
+=========================================== +
"""
from Nodo import Node
from colorama import init, Fore, Style
# Inicializar colorama
init(autoreset=True)

class ActionHistory:
    def __init__(self):
        self.head = None
        self.tail = None
        self.current = None
        
    def add_action(self, action, type_of_action):
        """Agrega una nueva acción al final."""
        new_node = Node(action, type_of_action)
        # Si la lista está vacía, inicializa el head y tail
        # y establece el current en el nuevo nodo
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            self.current = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
            self.current = new_node
        

    def move_forward(self):
        """Mover al siguiente nodo (rehacer)."""
        if self.current and self.current.next:
            self.current = self.current.next
            print(f"Avanzar a: {self.current.action}")
        else:
            print("No hay siguiente acción.")

    def move_backward(self):
        """Mover al nodo anterior (deshacer)."""
        if self.current and self.current.prev:
            self.current = self.current.prev
            print(f"Retroceder a: {self.current.action}")
        else:
            print("No hay acción anterior.")

    def show_from_start(self):
        """Mostrar toda la lista desde el inicio."""
        print("\nHistorial completo:")
        node = self.head
        while node:
            indicator = "<- Actual" if node == self.current else ""
            
            print(f"{Fore.GREEN}{node.type_of_action}{Style.RESET_ALL} {Fore.BLUE}{node.action}{Style.RESET_ALL} {Fore.YELLOW}{indicator}{Style.RESET_ALL}")
            node = node.next
        print()

    def show_from_current_backward(self):
        """Mostrar acciones hacia atrás desde donde estoy."""
        print("\nHistorial hacia atrás desde la acción actual:")
        node = self.current
        while node:
            print(node.action)
            node = node.prev
        print()

    def show_from_current_forward(self):
        """Mostrar acciones hacia adelante desde donde estoy."""
        print("\nHistorial hacia adelante desde la acción actual:")
        node = self.current
        while node:
            print(node.action)
            node = node.next
        print()
