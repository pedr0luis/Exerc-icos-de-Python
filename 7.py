A = float(input("Digite tamanho em m² a ser pintado: "))
L = A * 3 #quantidade de Litros a serem usadas
L = round(L) #arredondando o número de Litro
if (L<=18):
    print("Total a pagar será: R$ 18.00.")
else:
    print("Total a pagar será: R$ %.2f."%((L//18)*80))
