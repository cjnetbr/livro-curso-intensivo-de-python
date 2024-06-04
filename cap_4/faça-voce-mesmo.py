'''
FAÇA VOCÊ MESMO
4.1 - Pizzas: Pense em pelo menos três tipos de pizzas favoritas. Armazene os nomes dessas pizzas e, então, utilize um laço for para exibir o nome de cada pizza. 
• Modifique seu laço for para mostrar uma frase usando o nome da pizza em vez de exibir apenas o nome dela. Para cada pizza, você deve ter uma linha na saída 
contendo uma frase simples como Gosto de pizza de pepperoni.
• Acrescente uma linha no final de seu programa, fora do laço for, que informe quanto você gosta de pizza. A saída deve ser constituída de três ou mais linhas 
sobre os tipos de pizza que você gosta e de uma frase adicional, por exemplo, Eu realmente adoro pizza!

4.2 - Animais: Pense em pelo menos três animais diferentes que tenham uma característica em comum. Armazene os nomes desses animais em uma lista e, 
então, utilize um laço for para exibir o nome de cada animal.

• Modifique seu programa para exibir uma frase sobre cada animal, por exemplo, Um cachorro seria um ótimo animal de estimação.
• Acrescente uma linha no final de seu programa informando o que esses animais têm em comum. Você poderia exibir uma frase como 
Qualquer um desses animais seria um ótimo animal de estimação!

'''
#4.1 - Pizzas: Pense em pelo menos três tipos de pizzas favoritas. Armazene os nomes dessas pizzas e, então, 
# utilize um laço for para exibir o nome de cada pizza. 
pizzas = ['peperoni', 'calabresa', 'atum']

for pizza in pizzas:
    print(pizza)

print()
'''
Modifique seu laço for para mostrar uma frase usando o nome da pizza em vez de exibir apenas o nome dela. 
Para cada pizza, você deve ter uma linha na saída contendo uma frase simples como Gosto de pizza de pepperoni. 
'''

for pizza in pizzas:
    print(f"Gosto de pizza de {pizza}")

print()

'''
Acrescente uma linha no final de seu programa, fora do laço for, que informe quanto você gosta de pizza. 
A saída deve ser constituída de três ou mais linhas sobre os tipos de pizza que você gosta e de uma frase 
adicional, por exemplo, Eu realmente adoro pizza!
'''
for pizza in pizzas:
    print(f"Gosto de pizza de {pizza}")

print(f"Eu realmente adoro pizza!")

'''
Animais: Pense em pelo menos três animais diferentes que tenham uma característica em comum. Armazene os nomes desses animais em uma lista e, 
então, utilize um laço for para exibir o nome de cada animal.
'''
print()

animais = ['gato', 'cachorro', 'papagaio']

for animal in animais:
    print(animal)

'''
• Modifique seu programa para exibir uma frase sobre cada animal, por exemplo, Um cachorro seria um ótimo animal de estimação.
'''
print()

for animal in animais:
    print(f"Um {animal} seria um ótimo animal de estimação.")

'''    
• Acrescente uma linha no final de seu programa informando o que esses animais têm em comum. Você poderia exibir uma frase como 
Qualquer um desses animais seria um ótimo animal de estimação!
'''
print()

for animal in animais:
    print(f"Um {animal} seria um ótimo animal de estimação.")

print(f"Qualquer um desses animais seria um ótimo animal de estimação!")