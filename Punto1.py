def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Error: División por cero no permitida."

def ingreso_datos():
    operacion = input('Ingrese la operación que desea realizar (+ - * /): ')
    
    try:
        a = float(input('Ingrese el primer número: '))
        b = float(input('Ingrese el segundo número: '))
    except ValueError:
        raise ValueError("Error: Los valores ingresados deben ser números.")

    if operacion not in ['+', '-', '*', '/']:
        raise ValueError("Operación no válida. Debe ser +, -, *, o /")

    return operacion, a, b

if __name__ == '__main__':
    try:
        operacion, a, b = ingreso_datos()

        if operacion == '+':
            resultado = suma(a, b)
        elif operacion == '-':
            resultado = resta(a, b)
        elif operacion == '*':
            resultado = multiplicacion(a, b)
        elif operacion == '/':
            resultado = division(a, b)

        print(f'El resultado de la operación {operacion} es: {resultado}')
        
    except ValueError as ve:
        print(f"Error: {str(ve)}")
    except Exception as e:
        print(f"Ocurrió un error: {str(e)}")
