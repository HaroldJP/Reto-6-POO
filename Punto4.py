def mayor_suma_consecutiva(lista):
    try:
        # Verificar si la lista tiene al menos dos elementos
        if len(lista) < 2:
            raise ValueError('La lista debe contener por lo menos dos elementos.')
        
        # Calcular la mayor suma consecutiva
        max_suma = lista[0] + lista[1]
        for i in range(1, len(lista) - 1):
            suma_actual = lista[i] + lista[i + 1]
            if suma_actual > max_suma:
                max_suma = suma_actual
                
        return max_suma
    
    except ValueError as ve:
        print(f"Error: {str(ve)}")
        return None
    except Exception as e:
        print(f"Ocurrió un error inesperado: {str(e)}")
        return None

def numeros():
    lista = []
    try:
        a = int(input("Ingrese cuántos números quiere agregar: "))
        if a <= 0:
            raise ValueError("Debe ingresar un número mayor que cero.")
        
        b = 1
        while b <= a:
            try:
                c = int(input("Ingrese un número entero: "))
                lista.append(c)
                b += 1
            except ValueError:
                print("Error: Debe ingresar un número entero válido.")
                
    except ValueError as ve:
        print(f"Error: {str(ve)}")
    except Exception as e:
        print(f"Ocurrió un error inesperado: {str(e)}")
    
    return lista

if __name__ == "__main__":
    lista_numeros = numeros()
    print("Lista de números:", lista_numeros)
    if lista_numeros and len(lista_numeros) >= 2:
        resultado = mayor_suma_consecutiva(lista_numeros)
        if resultado is not None:
            print("La mayor suma entre dos elementos consecutivos es:", resultado)
