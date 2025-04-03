#Declare la función add_two_numbers
def add_two_numbers ():
    num_one = 2
    num_two = 3
    total = num_one + num_two
    return total
print(add_two_numbers())

#El área de un círculo
def AreaCirculo():
    pi = 3.1416
    radio = 5
    area = pi * radio * radio
    print(area)
print(AreaCirculo())

#Escriba una función llamada add_all_nums
def add_all_nums (*args):
    total = 0
    for arg in args:
        if not isinstance(arg, (int, float)):
            return f"Error: '{arg}' no es un número. Por favor, proporciona solo valores numéricos."
        total += arg
    return total

#Convertir la temperatura °C a °F 
def convert_celsius_to_fahrenheit():
    celcius = float(input("Ingresa la temperatura en grados Celcius: "))
    Farenheit = (celcius * 1.8) + 32
    print(Farenheit)
print(convert_celsius_to_fahrenheit())

#Escriba una función llamada check-season
Mes = str(input("Ingrese el mes: "))
def ChecarTemporada():
    if Mes in ["Septiembre", "Octubre", "Noviembre"]:
        print("Otoño")
    elif Mes in ["Diciembre", "Enero", "Febrero"]:
        print("Invierno")
    elif Mes in ["Marzo", "Abril", "Mayo"]:
        print("Primavera")
    elif Mes in ["Junio", "Julio", "Agosto"]:
        print("Verano")
    else:
        print("No existe")

#Escriba una función llamada calculate_slope
def calculate_slope(x1, y1, x2, y2):
    return (y2-y1)/(x2-x1)

#Calcula la ecuacion cuadratica 
def solve_quadratic_eqn(a, b, c):
    sol1 = (-(b) + ((b)**2 - 4*a*c)**0.5)/(2*a)
    sol2 = (-(b) - ((b)**2 - 4*a*c)**0.5)/(2*a)
    print(f"Sol1 : {sol1}")
    print(f"Sol2 : {sol2}")

#Declara una función llamada print_list
def print_list(lst):
    for i in lst:
        print(i)
print_list([1, 2, 6, 8, 3])

#Declare una función llamada reverse_list
def reverse_list(lst):
    new_lst = []
    for i in range(-1, -(len(lst))-1, -1):
        new_lst.append(lst[i])
    return new_lst
print(reverse_list([1, 2, 3, 4]))

#Declare una función llamada capitalize_list_items
def capitalize_list_items(lst):
    new_lst = []
    for item in lst:
        new_lst.append(item.capitalize())
    return new_lst
print(capitalize_list_items(['hello', 'world']))

#Declara una función llamada add_item
def add_item(lst, item):
    lst.append(item)
    return lst
numbers = [2, 3, 7, 9]
print(add_item(numbers, 5))

#Declara una función llamada remove_item
def remove_item(lst, item):
    lst.remove(item)
    return lst


numbers = [2, 3, 7, 9]
print(remove_item(numbers, 3))

#Declara una función llamada suma_de_números
def sum_of_numbers(r):
    sum = 0
    for i in range(r+1):
        sum += i
    return sum


print(sum_of_numbers(5))

#Declara una función llamada suma_de_impares
def sum_of_odds(r):
    sum = 0
    for i in range(r+1):
        if i % 2 != 0:
            sum += i
    return sum

#Declara una función llamada suma_de_números_pares
def sum_of_numbers(r):
    sum = 0
    for i in range(r+1):
        if i % 2 == 0:
            sum += i
    return sum

print("revisado")