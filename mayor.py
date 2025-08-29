entrada = input("Ingrese números separados por coma: ")

try:
    # Convertir la entrada en lista de números
    numeros = [float(num) for num in entrada.split(',')]

    if not numeros:
        print("No se ingresaron números.")
    else:
        mayor = max(numeros)
        print(f"El mayor número ingresado es: {mayor}")
except ValueError:
    print("Por favor, ingrese solo números separados por coma.")
