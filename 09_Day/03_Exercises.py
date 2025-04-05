#Diccionario
person={
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
    }
#Revisa el diccionario 1
if "skills" in person:
    HabilidadMedia = len(person["skills"])//2
    print(person['skills'][HabilidadMedia])
else:
    print("Error")

#Revisa el diccionario 2
if "skills" in person:
    TienePython = "Python" in person['skills']
    print(TienePython)
else:
    print("Error")

#Habilidades
if 'skills' in person:
    skills = person['skills']
    if set(skills) == {'JavaScript', 'React'}:
        print('He is a front end developer')
    elif set(skills) >= {'Node', 'Python', 'MongoDB'}:
        print('He is a backend developer')
    elif set(skills) >= {'React', 'Node', 'MongoDB'}:
        print('He is a fullstack developer')
    else:
        print('unknown title')

#Casado
if person.get('is_married') and person.get('country') == 'Finland':
    print(person["first_name"], person['last_name'], "lives", "in", person["country"], "He is married")

print("revisado")