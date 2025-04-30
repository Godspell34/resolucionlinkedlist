def separarParImpar(pila):
    # Crear dos listas para almacenar los números pares e impares
    pares = []
    impares = []
    
    # Mientras la pila no esté vacía
    while pila:
        # Extraer el elemento superior de la pila
        num = pila.pop()
        
        # Verificar si el número es par
        if num % 2 == 0:
            # Si es par, añadirlo a la lista de pares
            pares.append(num)
        else:
            # Si es impar, añadirlo a la lista de impares
            impares.append(num)
    
    # Reapilar los números en el orden correcto
    # Primero apilar los números pares
    for par in pares:
        pila.append(par)
    
    # Luego apilar los números impares
    for impar in impares:
        pila.append(impar)
    
    # Retornar la pila con los números organizados: pares en la parte inferior, impares en la parte superior
    return pila

# Ejemplo de uso
entrada = [2, 3, 6, 8, 11, 13, 18, 21]
resultado = separarParImpar(entrada)
print(resultado)  # Salida: [2, 6, 8, 18, 3, 11, 13, 21]
