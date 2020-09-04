

# funcion normal
def factorial(n):
    fac = 1
    for num in range(1,n+1):
        fac = fac * num
    return fac

# funcio principal
n = int(input("ingrese numero factorial: "))

print(factorial(n))