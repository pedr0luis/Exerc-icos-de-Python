forca = ['''
  +------+
         |
         |
         |
         |
         |
+--------+ ''', '''
  +------+
  |      |
         |
         |
         |
         |
+--------+ ''', '''
  +------+
  |      |
  o      |
         |
         |
         |
+--------+ ''', '''
  +------+
  |      |
  o      |
  |      |
         |
         |
+--------+ ''', '''
  +------+
  |      |
  o      |
 /|      |
         |
         |
+--------+ ''', '''
  +------+
  |      |
  o      |
 /|\     |
         |
         |
+--------+ ''', '''
  +------+
  |      |
  o      |
 /|\     |
 /       |
         |
+--------+ ''', '''
  +------+
  |      |
  o      |
 /|\     |
 / \     |
         |
+--------+ ''']

certas = erradas = ''
C = E = 0
R = 1
import requests
palavras = requests.get('https://www.ime.usp.br/~pf/dicios/br-sem-acentos.txt').text.lower().split()

from random import choice
def escolhe(): return choice(palavras)

def desenha():
    print(forca[E])
    for c in sorteada:
        if c in certas:
            print(c, end = ' ')
        else: print('_', end=' ')
    print()
    
from string import digits, punctuation
def chute(letras):
  while True:
    letra = input('Digite uma letra: ').lower()
    if letra in letras:
      print(f'Você já tentou a letra {letra} na ', end ='')
      for c in range(len(letras)):
          if letra==letras[c]:
              print(f'{c+1}º rodada', end ='')
              break
      if letra in certas:
          print(f'. E acertou tente uma nova letra diferente de {letra}.')
      else: print(f'. E errou tente uma nova letra diferente de {letra}.')
    elif letra in digits + punctuation:
      if letra in digits:
          print(f'Você precisa digitar uma letra. "{letra}" é um número.')
      else:print(f'Você precisa digitar uma letra. "{letra}" é uma pontuação.')
    elif len(letra) != 1:
      print('Somente uma letra por jogada.')
    else:
      return letra

def ganhou():
  return set(sorteada) == set(certas)

sorteada = escolhe()
while True:
  desenha()
  letra = chute(certas + erradas)
  if letra in sorteada: 
      certas = certas + letra
      C +=1
  else: 
      erradas = erradas + letra
      E +=1
  if len(erradas) == len(forca):
    print(f'PERDEEUUUU!! A palavra era {sorteada}')
    print(f'A palavra foi {sorteada}')
    print('Deseja jogar novamente?')
    print('1- SIM ou qualquer outra coisa para SAIR')
    R= (input('R= '))
    certas = erradas = ''
    C = E = 0
    sorteada = escolhe()
    if R=='1':
      certas = erradas = ''
      sorteada = escolhe()
    else: break
  elif ganhou():
    print('você ACERTOUUUUU!!!')
    print(f'A palavra foi {sorteada}')
    print('Deseja jogar novamente?')
    print('1- SIM ou qualquer outra coisa para SAIR')
    R= (input('R= '))
    certas = erradas = ''
    C = E = 0
    sorteada = escolhe()
    if R=='1':
      certas = erradas = ''
      sorteada = escolhe()
    else: break

