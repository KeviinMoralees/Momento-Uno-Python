
numeros = []
for i in range(20):
    numero = int(input(f"Ingrese un número {i + 1} : "))
    numeros.append(numero)


multiplos_2 = []
multiplos_3 = []
multiplos_2y3 = []

for numero in numeros:
    if numero % 2 == 0:
        multiplos_2.append(numero)
    if numero % 3 == 0:
        multiplos_3.append(numero)
    if numero % 2 == 0 and numero % 3 == 0:
        multiplos_2y3.append(numero)

print("Los múltiplos de 2 son:", multiplos_2)
print("Los múltiplos de 3 son:", multiplos_3)
print("Los múltiplos de 2 y 3 son:", multiplos_2y3)