N = int(input('Digite um número: '))
H = 0
for C in range (N,0,-1):
    H = H + (1/C)
print(f'H = {H:.2f}.')
