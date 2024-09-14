def palindromo():
    try:
        palabra = input("Ingrese su palabra para verificar si es un palíndromo: ").strip()
        
        if not palabra.isalpha():
            raise ValueError("Error: La palabra debe contener solo letras.")

        palabra = palabra.lower()
        palabra_invertida = palabra[::-1]

        if palabra == palabra_invertida:
            print(f"La palabra '{palabra}' es un palíndromo.")
        else:
            print(f"La palabra '{palabra}' no es un palíndromo.")

    except ValueError as ve:
        print(ve)
    except Exception as e:
        print(f"Ocurrió un error inesperado: {str(e)}")

if __name__ == "__main__":
    palindromo()
