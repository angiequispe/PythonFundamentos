# 1. importacion de librerias
import os

# 2. constantes MAYUSCULAS

# 3. funciones
def sumar(a, b):
    """
    SUMAR realiza la suma de dos numeros
    """
    return a + b

def multiplicar(a, b):
    """
    MULTIPLICAR  realiza la multiplicacion de dos numeros
    Parameters
    ----------
    a : float
        Valor numerico `a`.
    b : float
        Segundo valor numerico `b`.
    Returns
    -------
    float
        Retorna la suma de `a` + `b` 
    """
    return a*b

def dividir(a, b):
    """
    DIVIDIR realiza la division de 2 numeros
    """
    try:
        return a/b
    except Exception as e:
        print(e)
        return 0

# 4. Programa principal
if __name__ == "__main__":    
    # ingreso de datos
    num1 = float(input('Ingrese el primer número: '))
    num2 = float(input('Ingrese el segundo número: '))

    s = sumar(num1, num2)
    m = multiplicar(num1, num2)
    d = dividir(num1, num2)

    print(f'La suma de los numeros es {s}')
    print('La multiplicacion de los numeros es {}'.format(m))
    print('La division de los numeros es {division}'.format(division=d))
    
    # try:
    #     d = dividir(num1, num2)
    #     print('La division de los numeros es {division}'.format(division=d))
    # except Exception as e:
    #     print(e)
    
    # print('la operacion de los numeros es', s )

    pass # pass no realiza ninguna accion


