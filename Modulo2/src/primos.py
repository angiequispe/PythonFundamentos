
# importacion de librerias

# constantes

# funciones y metodos

def es_primo(numero):
    primo = True

    for n in range(2, numero, 1):
        if numero % n ==0:
            primo = False
            break
    return primo

#  mi programa principal
# ingreso de numero por teclado
numero = int(input('Ingrese un numero: '))

# valido si es primo
primo = es_primo(numero)

# imprimo según validacion
if primo:
    print(f'el numero: {numero} es primo')
else:
    print(f'el numero: {numero} NO es primo')