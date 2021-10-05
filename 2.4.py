sexo = input('Digite M-Masculino, ou F-Feminino: ')
h = float(input('Digite altura em cm: '))
if (sexo=='F' or sexo=='f'):
    print(f'Peso ideal é {(62.1*h)-44.7} Kg.')
else:
    print(f'Peso ideal é {(72.7*h)-58} Kg.')
