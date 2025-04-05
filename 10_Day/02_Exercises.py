#Bucle para la suma de todos los numeros (1)
suma = 0
for numero in range(101):
    suma += numero
    print("La suma de todos los numeros es : ", suma)

#Bucle para la suma de todos los numeros (2)
SumaPares = 0
SumaImpares = 0
for numero in range(101):
    if numero % 2 == 0:
        SumaPares += numero
    else:
        numero % 3 == 0
        SumaImpares += numero
print("La suma de todos los pares es: ", SumaPares)
print("La suma de todos los impares es: ", SumaImpares)

print("revisado")