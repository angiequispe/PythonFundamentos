
# obteniendo valor por teclado
color = input('Ingrese Color de Semaforo:')
# pasando valor a minusculas
color = color.lower()

if color =='verde':
    print('pueden pasar')
elif color == 'rojo' or color == 'amarillo':
    print('no puede pasar')
else:
    print('no entiendo')