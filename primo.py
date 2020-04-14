n = int(input("Ingrese un numero: "))

def esPrimo(n):
    if n <= 1:
        return False

    else:
        for i in range(2, n):
            if n % i == 0:
                return False
        return True

x = esPrimo(n)

if x is True:
    print("Es primo")
else:
    print("No es primo")
