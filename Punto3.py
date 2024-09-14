lista = []

def es_primo(numero):
    if numero <= 1:
        return False
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False
    return True

def numeros():
    try:
        a = int(input("Ingrese cuántos números quiere agregar: "))
        if a <= 0:
            raise ValueError("El número debe ser mayor que cero.")
        
        b = 1
        while b <= a:
            try:
                c = int(input(f"Ingrese el número {b}: "))
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
    try:
        numeros()
        print("Lista completa:", lista)
        
        primos = [numero for numero in lista if es_primo(numero)]
        print("Números primos en la lista:", primos)
    except Exception as e:
        print(f"Ocurrió un error inesperado: {str(e)}")
