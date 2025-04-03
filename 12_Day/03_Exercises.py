#Llama a tu función shuffle_list
import random
def shuffle_list(lst):
    random.shuffle(lst)
    return lst

#Escriba una función que devuelva un array de siete números aleatorios
def seven_random():
    s = set()
    lst = []
    while True:
        if len(s) == 7:
            lst = s
            return lst
        n = random.randint(0, 10)
        s.add(n)

print("revisado")