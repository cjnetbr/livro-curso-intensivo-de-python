''' 
Conhecendo o mundo: Pense em  pelo menos 5 lugares 
do mundo que você gos taria de visitar:

1 - Armazene as localidades em uma lista. 
Certifique-se de  que a lista não esteja em ordem alfabetica.

'''

localidade = ['orlando' ,'veneza', 'paris', 'lisboa', 'bonito']

'''
2 - Exiba sua lista na ordem original. Não se preocupe em exibir
a lista de forma elegante; basta exibi-la como uma lista python pura.

'''

print(localidade)

'''
3 - utilize o sorted() para exibir sua lista em ordem alfabetica, 
sem modificar a lista propriamente dita

'''
print("\nLista ordenada")
print(sorted(localidade))

'''
4- Mostre que sua lista manteve sua ordem 
original exibindo-a novamente

'''
print("\nLista original continual inalterada")
print(localidade)

'''
5- Utilize sorted() para exibir sua lista em 
ordem alfabetica  inversa sem alterar a ordem da lista original

'''
print("\nLista ordenada inversa")
print(sorted(localidade, reverse=True))

'''
6- Mostre que sua lista manteve sua ordem 
original exibindo-a novamente

'''
print("\nLista original continual inalterada")
print(localidade)

'''
7- Utilize o reverse() para mudar a ordem de sua lista
Exiba a lita original para motrar que a odem mudou
'''

print("\nlista ordernada com reverse()")
localidade.reverse()
print(localidade)

print("\nLista original foi alterada")
print(localidade)

'''
8- Utilize o reverse() para mudar a ordem de sua lista
Novamente Exiba a lita para motrar que a lita voltou à 
sua ordem original
'''

print("\nlista ordernada com reverse() 2x")
localidade.reverse()
print(localidade)


print("\na lita voltou à sua ordem original")
print(localidade)

'''
9- Utilize o sort() para ordenar a sua lista
em ordem alfabetica  e exiba a lista original para mostrar 
que a ordem foi alterada permanentemente
'''
print("\nlista ordernada com sort()")
localidade.sort()
print(localidade)

print("\nLista original foi alterada")
print(localidade)

'''
10- Utilize o sort() para ordenar a sua lista
em ordem alfabetica inverssa e exiba a lista original para mostrar 
que a ordem foi alterada permanentemente
'''

print("\nlista ordernada inversamente com sort()")
localidade.sort(reverse=True)
print(localidade)

print("\nLista original foi alterada")
print(localidade)