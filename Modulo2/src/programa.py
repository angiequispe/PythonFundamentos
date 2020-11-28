import primos2

# importacion de subcarpeta
from func import primo3


if __name__ == "__main__":
    print('ejecutando desde archivo programa.py')
    # ingreso de numero por teclado
    numero = int(input('Ingrese un numero: '))

    # imprimo según validacion
    if primo3.es_primo(numero):
        print(f'el numero: {numero} es primo')
    else:
        print(f'el numero: {numero} NO es primo')