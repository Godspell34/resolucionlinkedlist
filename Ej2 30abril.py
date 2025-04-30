def ordena(pila):
    # Crear una lista temporal para almacenar los elementos de la pila
    lista_temporal = []
    
    # Transferir todos los elementos de la pila a la lista temporal
    while pila:
        lista_temporal.append(pila.pop())
    
    # Ordenar la lista temporal en orden descendente
    lista_temporal.sort(reverse=True)
    
    # Volver a apilar los elementos ordenados en la pila original
    for num in lista_temporal:
        pila.append(num)
    
    # Retornar la pila ordenada de mayor a menor
    return pila

# Solicitar al usuario que ingrese una lista de enteros
entrada_usuario = input("Ingrese una lista de enteros separados por comas: ")
# Convertir la entrada en una lista de enteros
entrada = [int(num) for num in entrada_usuario.split(",")]

# Llamar al método ordena y mostrar el resultado
resultado = ordena(entrada)
print("Salida:", resultado)  # Salida: lista ordenada de mayor a menor
