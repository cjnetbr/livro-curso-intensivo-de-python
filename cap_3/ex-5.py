#Removendo convidados lista  para jantar com del()
convidados = ["Iolanda", "Claudio", "Ana", "Eduardo"]

for convidado in convidados:
    print(f"{convidado}, hoje o almoço é por minha conta.")

print(f"{convidados[2]}, Infelismente não poderá comparecer\n")

novo_convidado = "Cristina"
convidados[2] = novo_convidado

for convidado in convidados:
    print(f"{convidado}, hoje o almoço é por minha conta.\n")
print("Encontrei uma Mesa Maior. Mais pessoas serão convidadas para o jantar.\n")
    
novos_convidados = ["Luiz", "Caetano", "Miguel"]

convidados.insert(0, novos_convidados[0])
convidados.insert(2, novos_convidados[1])
convidados.append(novos_convidados[2])

for convidado in convidados:
    print(f"{convidado}, hoje o almoço é por minha conta.\n")

print("A grana ficou Curta, Infelismente só poderei levar 2 pessoas para Jantar.\n")

remover = convidados.pop()
print(f"Sinto muito {remover}, mas não poderei leva-lo para jantar\n")
remover = convidados.pop()
print(f"Sinto muito {remover}, mas não poderei leva-lo para jantar\n")
remover = convidados.pop()
print(f"Sinto muito {remover}, mas não poderei leva-lo para jantar\n")
remover = convidados.pop()
print(f"Sinto muito {remover}, mas não poderei leva-lo para jantar\n")
remover = convidados.pop()
print(f"Sinto muito {remover}, mas não poderei leva-lo para jantar\n")

for convidado in convidados:
    print(f"{convidado}, hoje o almoço é por minha conta.\n")
    
del convidados[1]
del convidados[0]

print(convidados)