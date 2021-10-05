f = open (r'C:\Users\Pedro Luís\OneDrive - Fatec Centro Paula Souza\Desktop\Python\Aulas\x.txt', 'w')
for linha in range(1,101):
    f.write(f'{linha}\n')
f.close()
