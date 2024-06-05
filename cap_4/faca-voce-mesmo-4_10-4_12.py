''' 
FAÇA VOCÊ MESMO
4.10 - Fatias: Usando um dos programas que você escreveu neste capítulo, acrescente várias linhas no final do programa que façam o seguinte:
• Exiba a mensagem Os três primeiros itens da lista são: Em seguida, use uma fatia para exibir os três primeiros itens da lista desse programa.
• Exiba a mensagem Três itens do meio da lista são:. Use uma fatia para exibir três itens do meio da lista.
• Exiba a mensagem Os três últimos itens da lista são:. Use uma fatia para exibir Os três últimos itens da lista.
4.11 - Minhas pizzas, suas pizzas: Comece com seu programa do Exercício 4.1 (página 97). Faça uma cópia da lista de pizzas e chame-a de friend_pizzas. Então faça o seguinte:
• Adicione uma nova pizza à lista original.
•Adicione uma pizza diferente à lista friend_pizzas.
• Prove que você tem duas listas diferentes. Exiba a mensagem Minhas pizzas favoritas são:; em seguida, utilize um laço for para exibir a primeira lista. Exiba a mensagem As pizzas favoritas de meu amigo são:; em seguida, utilize um laço for para exibir a segunda lista. Certifique-se de que cada pizza nova esteja armazenada na lista apropriada.
4.12 - Mais laços: Todas as versões de foods.py nesta seção evitaram usar laços for para fazer exibições a fim de economizar espaço. Escolha uma versão de foods.py e escreva dois laços for para exibir cada lista de comidas.

'''
#4.10 - Fatias: Usando um dos programas que você escreveu neste capítulo, acrescente várias linhas no final do programa que façam o seguinte:
pizzas = ['peperoni', 'calabresa', 'atum', 'marguerita', 'muçarela', 'napolitana']

#• Exiba a mensagem Os três primeiros itens da lista são: Em seguida, use uma fatia para exibir os três primeiros itens da lista desse programa.
print(f"Os três primeiros itens da lista são:{pizzas[:3]}\n")

#• Exiba a mensagem Três itens do meio da lista são:. Use uma fatia para exibir três itens do meio da lista.
print(f"Três itens do meio da lista são:{pizzas[2:5]}\n")

#• Exiba a mensagem Os três últimos itens da lista são:. Use uma fatia para exibir Os três últimos itens da lista.
print(f"Os três últimos itens da lista são: {pizzas[3:]}\n")

#4.11 - Minhas pizzas, suas pizzas: Comece com seu programa do Exercício 4.1 (página 97). Faça uma cópia da lista de pizzas e chame-a de friend_pizzas. Então faça o seguinte:
friend_pizzas = pizzas[:]

#• Adicione uma nova pizza à lista original.
pizzas.append("quatro queijos")

#•Adicione uma pizza diferente à lista friend_pizzas.
friend_pizzas.append("caipira")

#• Prove que você tem duas listas diferentes. Exiba a mensagem Minhas pizzas favoritas são:;
print(f"Minhas pizzas favoritas são:{pizzas}\n") 

# em seguida, utilize um laço for para exibir a primeira lista. Exiba a mensagem As pizzas favoritas de meu amigo são:; 
for pizza in pizzas:
    print(pizza)    
print(f"As pizzas favoritas de meu amigo são: {friend_pizzas}\n")

# em seguida, utilize um laço for para exibir a segunda lista. Certifique-se de que cada pizza nova esteja armazenada na lista apropriada.
for f_pizza in friend_pizzas:
    print(f_pizza)
