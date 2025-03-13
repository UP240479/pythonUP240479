#Ejercicios Nivel 1

#1
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
print(len(it_companies))

#2
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
it_companies.add("Twitter")
print(it_companies)

#3
it_companies = {'Amazon', 'Oracle', 'IBM', 'Twitter', 'Microsoft', 'Google', 'Apple', 'Facebook'}
it_companies.update(["Youtube", "Wikipedia"])
print(it_companies)

#4
it_companies = {'Microsoft', 'Twitter', 'Facebook', 'Google', 'Youtube', 'Apple', 'Wikipedia', 'Oracle', 'Amazon', 'IBM'}
it_companies.remove("Wikipedia")
print(it_companies)

#5
print("Con remove quitamos un elemento de forma permanente del set")
print("Con Discard descartamos un elemento pro una sola vez, hasta que se vuelve a ejecutar")


#Ejercicios Nivel 2

#1
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
AB = A.union(B)
print(AB)

#2
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
print(A.intersection(B))

#3
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
print(A.issubset(B))

#4
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
print(A.isdisjoint(B))

#5
AB = A.union(B)
print(AB)
BA = B.union(A)
print(BA)

#6 y 7
print(B.symmetric_difference(A))
del A
del B
del AB
del BA

#Ejercicios Nivel 3

#1
age = [22, 19, 24, 25, 26, 24, 25, 24]
st = set(age)
print(st)
LongitudSt = len(st)
LongitudAges = len(age)


#2
print("La cadena es una secuencia de caracteres")
print("La lista es una coleccion ordenada y mutable de elementos")
print("La tupla es una coleccion de elementos ordenada, similar a una lista, pero es inmutable")
print("El set es una coleccion desordenada de elementos unicos")