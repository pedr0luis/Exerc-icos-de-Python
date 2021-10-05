# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

# Exercícios extras

# G. verbing
# Dada uma string, caso seu comprimento seja pelo menos 3,
# adiciona 'ing' no final
# Caso a string já termine em 'ing', acrescentará 'ly'.
def verbing(s):
  if len(s)<3:return s
  else:
    if s[len(s)-3]+s[len(s)-2]+s[len(s)-1]=='ing':
        palavra=s+'ly'
        return palavra
    else:
        palavra=s+'ing'
        return palavra

# H. not_bad
# Dada uma string, procura a primeira ocorrência de 'not' e 'bad'
# Se 'bad' aparece depois de 'not' troca 'not' ... 'bad' por 'good'
# Assim 'This dinner is not that bad!' retorna 'This dinner is good!'
def not_bad(s):
  n = s.find('not')
  b = s.find('bad')
  if b > n:
    s = s[:n] + 'good' + s[b+3:]
  return s

# I. inicio_final
# Divida cada string em dois pedaços.
# Se a string tiver um número ímpar de caracteres
# o primeiro pedaço terá um caracter a mais,
# Exemplo: 'abcde', divide-se em 'abc' e 'de'.
# Dadas 2 strings, a e b, retorna a string
# a_inicio + b_inicio + a_final + b_final
def inicio_final(a, b):
  T=len(a)
  if T%2==0:
    m=int(T/2)
    a_inicio=a[:m]
    a_final=a[m:]
    T=len(b)
    if T%2==0:
        m=int(T/2)
        b_inicio=b[:m]
        b_final=b[m:]
    else:
        m=int(T/2)+1
        b_inicio=b[:m]
        b_final=b[m:]
  else:
    m=int(T/2)+1
    a_inicio=a[:m]
    a_final=a[m:]
    T=len(b)
    if T%2==0:
        m=int(T/2)
        b_inicio=b[:m]
        b_final=b[m:]
    else:
        m=int(T/2)+1
        b_inicio=b[:m]
        b_final=b[m:]
  return f'{a_inicio}{b_inicio}{a_final}{b_final}'

# J. zeros finais
# Verifique quantos zeros há no final de um número inteiro positivo
# Exemplo: 10010 tem 1 zero no fim e 908007000 possui três
def zf(n):
  n=str(n)
  Z=0
  for c in range(len(n)):
    if n[c]=='0':
      Z+=1
    else:Z=0
  return Z

# K. conta 2
# Verifique quantas vezes o dígito 2 aparece entre 0 e n-1
# Exemplo: para n = 20 o dígito 2 aparece duas vezes entre 0 e 19
def conta2(n):
  V=0 #variável que conta o número 2#
  for c in range (1,n-1):
    s=str(c)
    for C in range (len(s)):
        if s[C] == '2':
          V+=1
  return V

# L. inicio em potencia de 2
# Dado um número inteiro positivo n retorne a primeira potência de 2
# que tenha o início igual a n
# Exemplo: para n = 65 retornará 16 pois 2**16 = 65536
def inip2(n):
  n=str(n)
  c=0
  T=len(str(n))
  while c!=-1:
    R=str(2**c)
    if n==R[:T]:
      return c
      break
    else:c+=1
    

def test(obtido, esperado):
  if obtido == esperado:
    prefixo = ' Parabéns!'
  else:
    prefixo = ' Ainda não'
  print ('%s obtido: %s esperado: %s' % (prefixo, repr(obtido), repr(esperado)))

def main():
  print ('verbing')
  test(verbing('hail'), 'hailing')
  test(verbing('swiming'), 'swimingly')
  test(verbing('do'), 'do')

  print ()
  print ('not_bad')
  test(not_bad('This movie is not so bad'), 'This movie is good')
  test(not_bad('This dinner is not that bad!'), 'This dinner is good!')
  test(not_bad('This tea is not hot'), 'This tea is not hot')
  test(not_bad("It's bad yet not"), "It's bad yet not")

  print ()
  print ('inicio_final')
  test(inicio_final('abcd', 'xy'), 'abxcdy')
  test(inicio_final('abcde', 'xyz'), 'abcxydez')
  test(inicio_final('Kitten', 'Donut'), 'KitDontenut')

  print ()
  print ('zeros finais')
  test(zf(10100100010000), 4)
  test(zf(90000000000000000010), 1)

  print ()
  print ('conta 2')
  test(conta2(20), 2)
  test(conta2(999), 300)
  test(conta2(555), 216)

  print ()
  print ('inicio p2')
  test(inip2(7), 46)
  test(inip2(133), 316)
  test(inip2(1024), 10)
  
if __name__ == '__main__':
  main()
