for C in range (20):
    N=int(input(f'Digite {C+1}° número: '))
    if C==0:
          Nm=N
          NM=N
    else:
        if N<Nm:
            Nm=N
        elif N>NM:
            NM=N
print(f'Dos vinte números digitados {Nm} foi o menor e {NM} o maior.')
        
