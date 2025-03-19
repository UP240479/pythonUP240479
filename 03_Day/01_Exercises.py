#Día 3
#Área triángulo (4)
base = float(input("ingresa el valor de la base:"))
altura = float(input("ingrese el valor de la altura:"))
area = 0.5 * base * altura
print("El area del triangulo es:",area)


#Perimetro de un triangulo (5)
lado = float(input("Ingrese el primer valor:"))
lado2 = float(input("Ingrese el segundo valor:"))
lado3 = float(input("Ingrese el tercer valor"))
per = lado + lado2 + lado3 
print("El perimetro del triangulo es:", per)


#Calculos de un rectangulo (6)
largo = float(input("Ingresa el largo del rectangulo:"))
ancho = float(input("Ingrese el ancho del rectangulo:"))
area = largo * ancho
per = 2*(largo + ancho) 
print("El perimetro de tu rectangulo es:", per)
print("El area de tu rectangulo es:", area)


#Area de un circulo (7)
pi = 3.1416
radio = float(input("Ingresa el radio del circulo:"))
area = pi * radio **2
print("El area de tu circulo es:", area)
circunferencia = 2 * pi * radio 
print("La circunferencia de tu circulo es:", circunferencia)


#Calcula la Pendiente (8)
m = 2 
b = -2 
intersecciony =  (0, b)
interseccionx = (-b / m, 0)
print("la Pendiente es:", m)
print("La Interseccion con el eje y es:", intersecciony)
print("La Interseccion con el eje x es:", interseccionx)


#Distancia euclidiana (9)
import math 
x1, y1 = 2, 2
x2, y2 = 6, 10
m = (y2 - y1)/(x2 - x1)
distancia = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
print("La Pendiente es:", m)
print("La Distancia Euclidiana es:", distancia)


#Comparar ambas pendientes (10)
m1 = (y2 - y1) / (x2 - x1)
m2 = 2
if m1 > m2: 
    comparacion = "La primera pendiente es mayor."
elif m1 < m2:
    comparacion = "La segunda pendiente es mayor."
else:
    comparacion = "Ambas pendientes son iguales."
print("Pendiente 1", m1)
print("Pendiente 2:", m2)
print("Distancia euclidiana:", distancia)
print(comparacion)


#Calcular valor de y (11)
import math
num = float(input("Ingresa un numero:"))
valory = num**2 +6*num + 9
if num == 0:
    print("y es igual a cero. Tu resultado es:", valory)
else: 
    print("Intenta con otro numero.")


#Comparacion de palabras (12)
palabra1 = "Python"
palabra2 = "Dragon"
longitud1 = len(palabra1)
longitud2 = len(palabra2)
print("La longitud de Python es:", longitud1)
print("La longitud de Dragon es:", longitud2)
if longitud1 > longitud2:
    print("La palabra Python es mas larga que Dragon.")
else: 
    print("La palabra Python no es mas larga que Dragon.")


#Operadora and (13)
verificacion = "on" in palabra1 and "on" in palabra2
print("on esta en Python y en Dragon:", verificacion)


#Jergon (14)
oracion = "Espero que este curso no este lleno de jerga"
#contienejerga = jerga in oracion 
#print("¿La oracion contiene jerga?", contienejerga) 
if "jerga" in oracion:
    print("Si se encuentra")
else: 
    print("No contiene jerga")


#On en Python y Dragon (15)
if "on" in palabra1 and "on" in palabra2:
    print("Si, on esta presente tanto en Python como en Dragon.")
else:
    print("No, no esta presente en ambas palabras.")


#Longitud del texto (16)
longitudtexto = longitud1
print("La longitud de Python es:", longitud1)
texto = str(float("123456789"))
print("La longitud del texto es:", len(texto))


#Numeros pares (17)
divisible = float(input("Ingresa un numero:"))
if divisible % 2 == 0:
    print("Es un numero par:", divisible)
else:
    print("Es un numero impar", divisible)


#18
floor = 7//3 == int(2.7)
print("¿El piso 7x3 es igual al valor 2.7?", floor)


#19 Tipo de 10 
tipode10= type("10")
tipode10entero= type(10)
if tipode10 == tipode10entero:
    print("Los dos son iguales.")
else:
    print("Los dos son distintos.")

#20 Comprobar si 9.8 es igual a 10
valorde98 = int("9.8")
if valorde98 == 10:
    print("El valor es igual a 10.")
else:
    print("El valor no es igual a 10.") #Preguntar a profe que es "Value error"

#21 Tarifa de horas
horas = float(input("Introduce tus horas:"))
tarifa = float(input("Intruduce tu tarifa por hora:"))
tupagosemanal= horas * tarifa
print("Tu pago de la semana es:", tupagosemanal)

#22 Segundos de vida
años = float(input("Ingrese el numero de años que has vivido:"))
segundosdevida = años * 365 *24 *3600
print("Los segundos que has vivido son:", segundosdevida)

#23 Tabla
print("N 1 N *2 *3")
for i in range(1, 6):
    print(i, 1, i, i**2, i**3)