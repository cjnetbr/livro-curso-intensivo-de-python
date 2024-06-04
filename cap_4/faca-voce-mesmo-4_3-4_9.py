#contando até 20
#for n in range(21):
#    print(n)

#criar um lista entre 1 e 1.000.000
um_milhao = [ m for m in range(1,1000001)]
#print(um_milhao)

#for m in um_milhao:
#    print(m)

#Somando um milhão min() max()
print(min(um_milhao))
print(max(um_milhao))
print(sum(um_milhao))

#criar lista de numero impares e liste-os
#n_impares = [n for n in range(1,21,2)]
n_impares = []
for n in range(1,21,2):
    n_impares.append(n)
print(n_impares)

print()
    
#criar uma lista de mutiplos de 3 ate 30 e exiba-os
#m_tres = [n*3 for n in range(1,31)]
m_tres = []
#for n in m_tres:
for n in range(1,31):
    #print(n)
    m_3 = n*3
    m_tres.append(m_3)
print(m_tres)

print()

#criar lita  dos 10 primeiros cubos de 1 a 10
#cubo = [n**3 for n in range(1,11)]
cubo = []
for n in range(1,11):
    cb = n**3
    cubo.append(cb)
print(cubo)

print()

#criar lita  comprehension dos 10 primeiros cubos de 1 a 10
cubo = [n**3 for n in range(1,11)]
print(cubo)