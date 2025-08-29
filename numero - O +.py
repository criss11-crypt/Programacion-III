print('______________________')
print('Cristofer Enmanuel Machado Guillen')
print('codigo USTR168322')
print('_________________')
# Crear la función para verificar si un número es positivo, negativo o cero
def verificar_numero(num):
    if num > 0:
        return "Positivo"
    elif num < 0:
        return "Negativo"
    else:
        return "Cero"

# Solicitar un número al usuario
num = int(input("Introduce un número: "))

# Imprimir el resultado
print(f"El número {num} es: {verificar_numero(num)}")