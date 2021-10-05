import random
listaI = []
listaII = []
listaIII = []
for C in range (10):
    nI = (random.randint(0,100))
    listaI.append(nI)
    nII = (random.randint(0,100))
    listaII.append(nII)
print(f'Lista I: {listaI}.')
print(f'Lista II: {listaII}.')
for C in range (10):
    listaIII.append(listaI[C])
    listaIII.append(listaII[C])
print(f'Lista III: {listaIII}.')
