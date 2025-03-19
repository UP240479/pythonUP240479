#Ejercicios Nivel 1

#1
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
print(len(it_companies))

#2
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
it_companies.add("Twitter")
print(it_companies)

#3
it_companies = {'Amazon', 'Oracle', 'IBM', 'Twitter', 'Microsoft', 'Google', 'Apple', 'Facebook'}
it_companies.update(["Youtube", "Wikipedia"])
print(it_companies)

#4
it_companies = {'Microsoft', 'Twitter', 'Facebook', 'Google', 'Youtube', 'Apple', 'Wikipedia', 'Oracle', 'Amazon', 'IBM'}
it_companies.remove("Wikipedia")
print(it_companies)

#5
print("Con remove quitamos un elemento de forma permanente del set")
print("Con Discard descartamos un elemento pro una sola vez, hasta que se vuelve a ejecutar")


