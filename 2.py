import random
impar = []
par = []
lista = []
for C in range (20):
    n = (random.randint(0,100))
    lista.append(n)
    if (n%2==0):
        par.append(n)
    else:
        impar.append(n)
print(f'Lista: {lista}.')
print(f'Lista ímpar {impar}.')
print(f'Lista par {par}.')
