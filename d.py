R = 0
lista = []
R = 0
P = 0
for c in range (18644,33088):
    palavra = str(c)
    for C in range (len(palavra)):
        if (palavra[C] !='7'):
            P = P + 1
        if (P == 5):
            for k in range (len(palavra)):
                if (palavra[k] in '2'):
                    R = R + 1
                    lista.append(palavra)
                    break
    P=0
print(f'Resposta: {R}.')
print(f'Lista gerada: {lista}')
