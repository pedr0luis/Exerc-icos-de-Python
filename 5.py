text = '''The Python Software Foundation and the global Python
community welcome and encourage participation by everyone. Our
community is based on mutual respect, tolerance, and encouragement, and
we are working to help each other live up to these principles. We want
our community to be more diverse: whoever you are, and whatever
your backgrou and, we welcome you.'''
text = text.replace(',','')
text = text.replace('.','')
text = text.replace(':','')
text = text.lower()
text = text.split()
lista = []
lista_nova = []
P = 0
for C in range (len(text)):
    palavra = text[C]
    if (len(palavra)>4):
        if palavra[0] in 'python':
            lista_nova.append(palavra)
            P = P + 1
        elif palavra[-1] in 'python':
            lista_nova.append(palavra)
            P = P + 1
print(f'Nova lista que tem "python": {lista_nova}. Exitem {P} palavras que começam, ou terminam com as letras: "python".')
