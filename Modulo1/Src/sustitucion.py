# importacion de modulos
import string

# definicion de constantes : BUSCAR Y REEMPLAZAR : CONTROL + H
ALFABETO = string.ascii_uppercase


# recuperando clave
clave = 'YTNSHKVEFXrBAUQZCLWDMIPGJO'
clave = clave.upper()

# leemos plaintext
plaintext = input('introduzca palabra a encriptar: ')


ciphertext = ''
for letra in plaintext:
    # algoritmo transformacion
    index_alfa = ALFABETO.find(letra.upper()) # posicion de letra en ALFABETO
    
    if index_alfa >= 0:
        if letra.isupper():
            letra = clave[index_alfa] # transformo letra segun indice encontrado
        else:
            letra = clave[index_alfa].lower()
    # Completando 'ciphertext' : 'a' + 'b'
    ciphertext += letra
print('El texto cifrado es: {}'.format(ciphertext))