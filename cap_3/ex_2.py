#Alterando lista de Convidados para jantar
convidados = ["Iolanda", "Claudio", "Ana", "Eduardo"]

for convidado in convidados:
    print(f"{convidado}, hoje o almoço é por minha conta.")

print(f"{convidados[2]}, Infelismente não poderá comparecer\n")

novo_convidado = "Cristina"
convidados[2] = novo_convidado

for convidado in convidados:
    print(f"{convidado}, hoje o almoço é por minha conta.\n")