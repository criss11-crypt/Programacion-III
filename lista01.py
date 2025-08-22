print ("_____________________________")
print("Lista - sumar todos")
print("_____________________________")

# solicitar un numero final de la lista
num1 = int(input("Ingrese un numero hasta 100: "))

# crear la lista desde 1 hasta num1
lista = list(range(1, num1+1))

# calcular la suma
resultado = sum(lista)

# imprimir el resultado
print(f"La suma de la lista hasta {num1} es {resultado}")