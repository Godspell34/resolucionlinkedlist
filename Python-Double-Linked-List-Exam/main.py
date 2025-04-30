"""
+=========================================== +
| AUTOR: ALEX DIAZ y SSLER FLORES            |
| FECHA: 25-04-2025                          |
| DESCRIPCIÓN: Funcion principal del repo    |
| VERSION: 1.0                               |
+=========================================== +
"""
from ActionHistoryManager import ActionHistory

def main():
    # Crear una instancia de ActionHistory
    action_history = ActionHistory()

    # Agregar acciones al historial
    action_history.add_action("Hello world", "Escribir")
    action_history.add_action("Hola", "Borrar")
    action_history.add_action("Este es nuestro mundo", "Copiar")

    # Mostrar el historial completo
    action_history.show_from_start()

    # Mover hacia adelante y hacia atrás en el historial
    action_history.move_backward()
    action_history.show_from_start()
    action_history.add_action("Nuevo texto", "Pegar")
    action_history.show_from_start()
    
main()