entrada = input("ingrese numeros separador por coma: ")

try:
    numeros not numeros = [float(num) for num in entrada.split(',')]

    if not numeros:
        print("no se ingresaron numeros.")
    else:
        mayor = max(numeros)
        print(f"el mayor numero ingresado es: {mayor}")
except valueError:
    print("por favor, ingrese solo numeros separador por coma.")

