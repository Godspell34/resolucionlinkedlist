def Convbinario(numero):
    # Crear una pila para almacenar los dígitos binarios
    pila = []
    
    # Manejar el caso especial para el número 0
    if numero == 0:
        return [0]
    
    # Convertir el número a binario utilizando la pila
    while numero > 0:
        # Obtener el residuo de la división entre 2 (dígito binario)
        residuo = numero % 2
        # Apilar el residuo en la pila
        pila.append(residuo)
        # Dividir el número entre 2 para continuar con el siguiente dígito
        numero //= 2
    
    # Crear una lista para almacenar el resultado en orden correcto
    binario = []
    
    # Desapilar los elementos para obtener el binario en el orden correcto
    while pila:
        binario.append(pila.pop())
    
    # Convertir la lista de dígitos binarios a una cadena y luego a una lista
    return [''.join(map(str, binario))]

# Solicitar al usuario que ingrese un número entero
entrada_numero = int(input("Ingrese un número entero para convertir a binario: "))

# Llamar al método Convbinario y mostrar el resultado
resultado_binario = Convbinario(entrada_numero)
print("Salida:", resultado_binario)  # Salida: representación en binario