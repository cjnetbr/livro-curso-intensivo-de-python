cars = ['bmw', 'audi', 'toyota', 'subaru']
#Ordena a lista em ordem alfabética de forma inrreversível
cars.sort()
print(cars)

#ordena a lista de forma reversa. Tbm de forma permanente
cars.sort(reverse=True)
print(cars)

#ordenanda a lista temporariamente com a função sorted
cars = ['bmw', 'audi', 'toyota', 'subaru']
print( "\nEsta é a lista original")
print(cars)

print("\nLista ordenada com a função 'sorted'")
print(sorted(cars))

print( "\na lista original continua inalterada")
print(cars)

