#Codigo que califique
Calificacion = int(input("Ingresa tu calificacion"))
if Calificacion >= 80 and Calificacion <= 100:
    print("Tu nota es A")
elif Calificacion >= 70 and Calificacion <= 79:
    print("Tu nota es B")
elif Calificacion >= 60 and Calificacion <= 69:
    print("Tu nota es C")
elif Calificacion >= 50 and Calificacion <= 59:
    print("Tu nota es D")
else:
    print("Tu nota es F")

#Comprobacion de temporada del año
Mes = str(input("Ingrese el mes: "))
if Mes in ["Septiembre", "Ocubre", "Noviembre"]:
    print("Otoño")
elif Mes in ["Diciembre", "Enero", "Febrero"]:
    print("Invierno")
elif Mes in ["Marzo", "Abril", "Mayo"]:
    print("Primavera")
elif Mes in ["Junio", "Julio", "Agosto"]:
    print("Verano")
else:
    print("No existe")

#Lista de frutas
fruits = ['banana', 'orange', 'mango', 'lemon']
chckfruit = str(input("Agrega el nombre de una fruta en ingles: "))
if chckfruit in fruits:
    print("Esa fruta ya existe en la lista")
else:
    fruits.append(chckfruit)
    print(fruits) 

print("revisado")