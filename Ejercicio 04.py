#Concatenarpalabras (1)
Primera_palabra  = "Treinta"
Segunda_palabra = "dias"
Tercera_palabra = "de"
Cuarta_palabra = "Python"
Espacio = " "
FraseCompleta = Primera_palabra + Espacio + Segunda_palabra + Espacio + Tercera_palabra + Espacio + Cuarta_palabra
print (FraseCompleta)

#Concatenar una cadena (2)
PrimeraPalabra = "Codificacion"
SegundaPalabra = "para"
TerceraPalabra = "todos"
Frase = PrimeraPalabra + Espacio + SegundaPalabra + Espacio + TerceraPalabra
print(Frase)

#empresa (3)
Empresa = Frase

#empresa (4)
print (Empresa)

#empresa (5)
print(len(Empresa))

#empresa(6)
print(Empresa.upper())

#empresa (7)
print(Empresa.lower)

#metodo capitalizar (8)
print(Frase.capitalize())
print(Frase.title())
print(Frase.swapcase())

#Recortar (9)
Destajada = Empresa[12:]
print(Destajada)

#cadena codificacion (10)
Subcadena = Frase
print(Subcadena.find("Codificacion")) 

#Reemplace la palabra codificación (11)
print(Empresa.replace("Codificacion", "Python"))

#Cambie Python (12)
print(Empresa.replace("Codificacion para todos", "Python para todos"))

#Divida la cadena 'Coding For All' (13)
Cadena = Frase
print(Cadena.split())
Cadena = "Codificacion, para, todos"
print(Cadena.split(" , "))

#"Facebook, Google, Microsoft, etc (14)
A1 = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print(A1.split())
A1 = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print(A1.split(" , "))

#¿Cuál es el carácter en el índice 0 en la cadena Codificación para todos ? (15)
Frase = "Codificacion para todos"
print(Frase[0])

#¿Cuál es el último índice de la cadena Codificación Para Todos ? (16)
Frase = "Codificacion para todos"
print(Frase[22])

#¿Qué carácter está en el índice 10 en la cadena "Codificación para todos"? (17)
Frase = "Codificacion para todos"
print(Frase[10])

#Crea un acrónimo o una abreviatura (18)
Acronimo = "PPT"

#Crea un acrónimo o una abreviatura2 (19)
Acronimo = "CFA"

#Utilice el índice para determinar la posición (20)
Frase = "Codificacion para todos"
print(Frase.find("C"))

#Utilice el índice para determinar la posición2 (21)
Frase = "Codificacion para todos"
print(Frase.find("f"))

#Utilice rfind para determinar la posición (22)
Frase = "Codificacion para todos"
print(Frase.rfind("i"))

#Utilice index o find para encontrar la posición (23)
Frase = "No puedes terminar una oración con porque porque porque es una conjunción"
print(Frase.find("porque"))

#Utilice rindex para encontrar la posición (24)
Frase = 'No puedes terminar una oración con porque porque porque es una conjunción'
print(Frase.rfind("porque"))

#Elimina la frase 'porque porque porque' (25)
Frase =  'No puedes terminar una oración con porque porque porque es una conjunción'
print("Frase")
primer_porque = Frase [0:31]
print(primer_porque)
ultimo_porque = Frase [54:]
print(ultimo_porque) 

#Encuentra la posición de la primera aparición de la palabra (26)
Frase = 'No puedes terminar una oración con porque porque porque es una conjunción'
print(Frase.find("porque"))

#Elimina la frase 'porque porque porque' (27)
Frase = 'No puedes terminar una oración con porque porque porque es una conjunción'
print("Frase")
primer_porque = Frase [0:31]
print(primer_porque)
ultimo_porque = Frase [54:]
print(ultimo_porque)

#¿''Coding For All' comienza con una subcadena Coding ? (28)
Frase = "Codificacion para todos"
print(Frase.startswith("Codificacion"))

#¿'Coding For All' termina con una subcadena 'coding '? (29)
Frase = "Codificacion para todos"
print(Frase.endswith("Codificacion"))

#'Codificación para todos' (30)
Frase = "      Codificacion para todos      "
print(Frase.strip("       "))

#¿Cuál de las siguientes variables devuelve Verdadero cuando usamos el método isidentifier()? (31)
Frase = "30 dias de Python"
print(Frase.isidentifier())
Frase = "Treinta dias de Python"
print(Frase.isidentifier())

#Biblioteca (32)
lib =  ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
Resultado = " # ".join(lib)
print(Resultado)

#Utilice la secuencia de escape (33)
print("I\nam\nenjoying\nthis\nchallenge.")
print("I\njust\nwonder\nwhat\nis\nnext.")

#Utilice una secuencia de escape2 (34)
#Name      Age     Country   City
#Asabeneh  250     Finland   Helsinki
print("Name\tAge\tCountry\tCity")
print("Asabeneh\t250\tFinland\tHelsinki")

#Utilice el método de formato de cadena para mostrar lo siguiente: (35)
radius = 10
area = 3.14 * radius ** 2
formated_string = 'The area of circle with a radius %d is %.2f.' %(radius, area)
print(formated_string)

#Realice lo siguiente utilizando métodos de formato de cadene (36)
#8 + 6 = 14
#8 - 6 = 2
#8 * 6 = 48
#8 / 6 = 1.33
#8 % 6 = 2
#8 // 6 = 1
#8 ** 6 = 262144
a = 8
b = 6
suma = a + b
resta = a - b
Multiplicacion = a * b
Division = a / b
Porcentaje = a % b
Potencia = a ** b
Divf = a // b