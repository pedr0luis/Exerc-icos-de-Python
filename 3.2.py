N = int(input('Digite um número:'))
for C in range (1,N):
    if (C*C==N):
        R = C
print(f'Número que mais se aproxima da raiz de {N} é: {R}².')
