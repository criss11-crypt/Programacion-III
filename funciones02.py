# Crear la función para sumar dos números
def suma(num1, num2):
    return num1 + num2

# Solicitar los números al usuario
num1 = int(input("Introduce el primer número: "))
num2 = int(input("Introduce el segundo número: "))

# Imprimir los resultados
print(f'La suma de {num1} y {num2} es: {suma(num1, num2)}')