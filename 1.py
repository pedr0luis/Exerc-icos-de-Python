import random
lista = []
max=0
min=100
for C in range (10):
    n = (random.randint(0,100))
    lista.append(n)
    if (max<n):
        max=n
    if (min>n):
        min=n
print(lista)
print(f'Menor: {min}.')
print(f'Maior: {max}.')
