#Bucle 1
numeros = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for number in numeros:
    print(number)

contar = 0
while contar < 11:
    print(contar)
    contar = contar +1

#Bucle 2
Numero = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
for number in Numero:
    print(number)

contar = 0
while contar > 11:
    print(contar)
    contar = contar - 1

#Bucle 3
for i in range(1, 8):
    print('#' * i)

    #Bucles anidados
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
gato = "# "
for i in range(4):
    print(gato * i)

#Imprima el siguiente patrón:
#0 x 0 = 0
#1 x 1 = 1
#2 x 2 = 4
#3 x 3 = 9
#4 x 4 = 16
#5 x 5 = 25
#6 x 6 = 36
#7 x 7 = 49
#8 x 8 = 64
#9 x 9 = 81
#10 x 10 = 100

i = 0
contar = 0
while contar < 11:
    mult = i*i
    print(i, "x", i, mult)
    i = i + 1
    contar = contar + 1

#Itere a través de la lista
lista = ['Python', 'Numpy', 'Pandas', 'Django', 'Flask']
for iterator in lista:
    print(lista)

#Utilice el bucle for para iterar de 0 a 100 (1)
for numero in range(101):
    if numero % 2 == 0:
        print (numero)

#Utilice el bucle for para iterar de 0 a 100 (2)
for numero in range(101): 
    if numero % 2 != 0:
        print(numero)

print("revisado")