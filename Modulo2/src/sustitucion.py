import string
import sys


# obteniendo argumento clave
sustitucion = sys.argv[1]
# convirtiendo cadena sutituion a mayusculas
sustitucion = sustitucion.upper()


mensaje = input('Ingrese mensaje a encriptar: ')

# abecedario
abecedario = string.ascii_uppercase

ciphertext=''
for letra in mensaje:
    if letra.upper() in abecedario and letra.islower():
        index = abecedario.find(letra.upper())
        ciphertext +=  sustitucion[index].lower()
        continue
    elif letra.upper() in abecedario and letra.isupper():
        index = abecedario.find(letra.upper())
        ciphertext +=  sustitucion[index]
        continue
    ciphertext +=  letra

print('ciphertext:',ciphertext)
