#Nueva lista de paises
countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

upper_countries = map(lambda country: country.upper(), countries)
print(list(upper_countries))

#Nueva lista de numeros
squares = map(lambda x: x*x, numbers)
print(list(squares))

#Nueva lista de nombres
upper_names = map(lambda name: name.upper(), names)
print(list(upper_names))

#Filtrar paises con "land"
def is_land(s):
    if 'land' in s:
        return True
    else:
        return False
land = filter(is_land, countries)
print(list(land))

#Filtrar paises con 6 letras
def SeisLetras(s):
    if len(s) == 6:
        return True
    else:
        return False
Seis = filter(SeisLetras, countries)
print(list(Seis))

#Filtrar paises que empiecen con "E"
def EmpiezaCon(s):
    if s[0] == "E":
        return True
    else: 
        return False
    
Empieza = filter(EmpiezaCon, countries)
print(list(Empieza))

#Encadenar dos o más iteradores de lista  
#Declare una función llamada get_string_lists 
def get_string_lists(lst):
    new = []
    for item in lst:
        if type(item) == str:
            new.append(item)
    return new


print(get_string_lists([1, 2, 3, 4, 5, 7, 'hllo']))

print("revisado")