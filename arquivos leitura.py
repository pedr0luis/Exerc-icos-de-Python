f = open (r'C:\Users\Pedro Luís\OneDrive - Fatec Centro Paula Souza\Desktop\Python\Aulas\x.txt')
for linha in f.readlines():
    print(linha.strip())
f.close()
