

print("Bienvenido a la calculadora virtual")

while(True):
    print("""Elija alguna opción a operar
    1) Sumar do numeros
    2) Restar dos numeros
    3) Multiplicar dos numeros""")
    # obteniendo valor por teclado
    opcion = input()
    
    if opcion == '1':
        n1 = float(input("Introduce el primer número: "))
        n2 = float(input("Introduce el segundo número: "))
        print("El resultado de la suma es: ",n1+n2)
        break
    elif opcion == '2':
        n1 = float(input("Introduce el primer número: "))
        n2 = float(input("Introduce el segundo número: "))
        print("El resultado de la suma es: ",n1-n2)
        break
    elif opcion =='3':
        n1 = float(input("Introduce el primer número: "))
        n2 = float(input("Introduce el segundo número: "))
        print("El resultado de la suma es: ",n1*n2)
        break
    else:
        print("opción invalida, vuelve a intentarlo")
