N = int(input('Digite um número:'))
R=1
for C in range (2,N+1):
    R = R * C
print(f'{N}! = {R}.')
