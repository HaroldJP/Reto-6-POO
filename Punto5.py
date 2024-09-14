def tienen_mismos_caracteres(palabra1, palabra2):
    # Ordenamos los caracteres de ambas palabras y los comparamos
    return sorted(palabra1) == sorted(palabra2)

def palabras_con_mismos_caracteres(lista):
    if not isinstance(lista, list):
        raise TypeError("La entrada debe ser una lista.")
    
    if any(not isinstance(palabra, str) for palabra in lista):
        raise ValueError("Todos los elementos de la lista deben ser cadenas de texto.")
    
    resultado = []
    lista = [palabra.strip() for palabra in lista if palabra.strip()]  # Eliminamos palabras vacías
    for i in range(len(lista)):
        palabra_actual = lista[i]
        misma_palabra = False
        for j in range(i + 1, len(lista)):
            if tienen_mismos_caracteres(palabra_actual, lista[j]):
                misma_palabra = True
                break
        if misma_palabra:
            resultado.append(palabra_actual)
    return resultado

def main():
    try:
        entrada = input("Ingrese la lista de palabras separadas por comas: ")
        lista = entrada.split(",")
        lista = [palabra.strip() for palabra in lista if palabra.strip()]  # Eliminamos palabras vacías
        if not lista:
            raise ValueError("La lista no debe estar vacía.")
        
        palabras_con_mismos = palabras_con_mismos_caracteres(lista)
        print("Palabras con los mismos caracteres:", palabras_con_mismos)
    
    except (ValueError, TypeError) as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
