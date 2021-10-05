texto = open ('exercicio.txt','r')
cripto = open ('cripto', 'w')

for linha in texto.readlines():
    for letra in linha:
        if letra in 'aeiouãõ':
            cripto.write('*')
        else:
            cripto.write(letra)
texto.close()
cripto.close()
