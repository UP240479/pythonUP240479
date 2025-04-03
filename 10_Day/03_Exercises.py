
#Carpeta de datos de paises
from countries import countries_list
paises = countries_list.countries
landCountries = []
for land in paises:
    if "land" in land: 
        landCountries.append(land)  
print("Países con 'land': ", landCountries)

#Carpeta de lista de frutas
fruit = ['banana', 'orange', 'mango', 'lemon']
reversa = []
for i in range(len(fruit) - 1, -1, -1):  
    reversa.append(fruit[i])

print(reversa)

#Iformacion de folder
import paisesinfo as p
datos = p.aaa

#Numero total de lenguas (1)
idiomas = []
for pais in datos:
    for lenguaje in pais['languages']:
        idiomas.append(lenguaje)        
        
print('lenguajes totales: ', len(idiomas))

#Numero total de lenguas (2)
setidiomas = set(idiomas)
dctidiomas = {}
for language in setidiomas:
    dctidiomas[language] = 0
for idioma in dctidiomas:
    for pais in datos:  
         if idioma in pais['languages']:
             dctidiomas[idioma] = pais['population'] + dctidiomas[idioma]
svLanguagePop = sorted(dctidiomas.values(), reverse= True)
skLanguagePop = sorted(dctidiomas, key= dctidiomas.get, reverse=True)
j = 0
for top in range(10):
    print( skLanguagePop[j], ": ",svLanguagePop[j])
    j+= 1

#10 paises mas populares en el mundo
from paisesinfo import aaa 
ordenados = sorted(aaa, key=lambda item: item['population'], reverse=True)
print("Top 10 países más poblados:\n")
for pais in ordenados[:10]:
    print(pais['name'], pais['population'])

print("revisado")