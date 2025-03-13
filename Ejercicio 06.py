#Ejercicios nivel 1

#1
print("")
empty =()

#2
print("")
print("Introduce dos listas de nombres de tus hermanos:")
sisters = ("Naomi")
brothers = ("Yuyin, Panita")
print("Lista de hermanos:", brothers)
print("Lista de hermanas:", sisters)

#3
print("")
print("Lista unida de hermanos")
siblings = sisters + brothers
print(siblings)

#4
print("")
print("¿Cuantos hermanos tengo?")
nsiblings = len(siblings)
print(nsiblings)

#5
parents = ("Claudia, Siloni")
family = (brothers+sisters+parents)

#Ejercicio nivel 2

#1
family
padres = family [2:4]
desempaque = family [0:2]
print(padres)
print(desempaque)

#2
frutas = ("Pera, Manzana, Melon, Sandia")
verduras = ("Tomate, Calabaza, Jitomate, Zanahoria")
productosanimales = ("Huevo, Queso, Leche, Carne")
food_stuff_tp = (frutas + verduras + productosanimales)
print (food_stuff_tp)

#3
food_stuff_lt = ("Manzana, Melon, Pera, Sandia, Tomate, Calabaza, Jitomate, Zanahoria, Huevo, Queso, Leche, Carne")
primerelemento = food_stuff_lt [5]
segundoelemento = food_stuff_lt [6]
print(primerelemento)
print(segundoelemento)

#4
separacion1 = food_stuff_lt [0:2]
separacion2 = food_stuff_lt [9:11]
print(separacion1)
print(separacion2)

#5
del food_stuff_tp

#6
paisesnordicos = ("Denmark", "Iceland", "Finland", "Norway", "Sweden")
print("Estonia" in paisesnordicos)
print("Iceland" in paisesnordicos)