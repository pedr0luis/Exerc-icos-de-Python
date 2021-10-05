N = int(input('Digite um número:'))
R=0
for C in range (1,N+1):
    if (N%C==0):
        R+=1
    if (R>2):
        break
if (R==2):
    print(f'{N} é um número primo.')
else:
    print(f'{N} não é um número primo.')
