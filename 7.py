Mes = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho', 'julho', 'agosoto', 'setembro', 'outubro', 'novembro','dezembro']
M=0
while (M<1) and (M>12):
    M = int(input('Digite um número entre 1 e 12: '))
    if (M<1) and (M>12):
        print('Mes inválido. Digite novamente!')

