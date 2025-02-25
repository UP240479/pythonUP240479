#Día 3
#Área triángulo 
base = float(input("ingresa el valor de la base:"))
altura = float(input("ingrese el valor de la altura:"))
area = 0.5 * base * altura
print("El area del triangulo es:",area)

#Perimetro de un triangulo
lado = float(input("Ingrese el primer valor:"))
lado2 = float(input("Ingrese el segundo valor:"))
lado3 = float(input("Ingrese el tercer valor"))
per = lado + lado2 + lado3 
print("El perimetro del triangulo es:", per)

#Calculos de un rectangulo
largo = float(input("Ingresa el largo del rectangulo:"))
ancho = float(input("Ingrese el ancho del rectangulo:"))
area = largo * ancho
per = 2*(largo + ancho) 
print("El perimetro de tu rectangulo es:", per)
print("El area de tu rectangulo es:", area)

#Area de un circulo 
pi = 3.1416
radio = float(input("Ingresa el radio del circulo:"))
area = pi * radio **2
print("El area de tu circulo es:", area)
circunferencia = 2 * pi * radio 
print("La circunferencia de tu circulo es:", circunferencia)

#Calcula la Pendiente
m = 2 
b = -2 
intersecciony =  (0, b)
interseccionx = (-b / m, 0)
print("la Pendiente es:", m)
print("La Interseccion con el eje y es:", intersecciony)
print("La Interseccion con el eje x es:", interseccionx)

#Distancia euclidiana
import math 
x1, y1 = 2, 2
x2, y2 = 6, 10
m = (y2 - y1)/(x2 - x1)
distancia = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
print("La Pendiente es:", m)
print("La Distancia Euclidiana es:", distancia)

#Comparar ambas pendientes
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

#Calcular valor de y
import math
def calcular_y(x):
    return x**2 + 6*x + 9
ejemplox = [-5, -3, 0, 2, 5]
print("Valores de Y para diferentes X:")
for x in ejemplox:
    print("Para x:{x}, y={calcular_y(x)}")
a, b, c = 1, 6, 9
x_raiz1 = (-b + math.sqrt(b**2 - 4*a*c)) / (2*a)
x_raiz2 = (-b - math.sqrt(b**2 - 4*a*c)) / (2*a)
print("El valor de x donde y=0 es: X={x_raiz1} y x={x_raiz2}")

