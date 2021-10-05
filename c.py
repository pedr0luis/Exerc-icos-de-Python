R = 0
for C in range (1067,3628):
    if (C%2==0) and (C%7==0):
        R =  R + 1
print(f'Resposta: {R}.')
