

# funcion recursiva

def factorial_recursivo(n):
    # logica
    if n==1:
        return 1
    else:
        return n * factorial_recursivo(n-1)

# funcio principal
n = int(input("ingrese numero factorial: "))

print(factorial_recursivo(n))