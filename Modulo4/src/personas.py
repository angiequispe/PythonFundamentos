import os

texto = """1;Carlos;Pérez;05/01/1989
2;Manuel;Heredia;26/12/1973
3;Rosa;Campos;12/06/1961
4;David;García;25/07/2006
"""


if 'personas.txt' not in os.listdir():
    # escribiendo fichero
    with open('personas.txt',mode='w') as f:
        f.write(texto)

# leyendo data
personas = []
with open('personas.txt',mode='r') as f:
    for line in f.readlines():
        lista = line.split(';')
        dicx_personas ={}
        dicx_personas['index'] = lista[0]
        dicx_personas['nombre'] = lista[1]
        dicx_personas['apellido'] = lista[2]
        dicx_personas['fecha'] = lista[3].strip()
        
        personas.append(dicx_personas)
        
# imprimiendo data
for person in personas:
    print("""index: {index}
            nombre: {nombre}
            apellido: {apellido}
            fecha: {fecha}""".format(**person))