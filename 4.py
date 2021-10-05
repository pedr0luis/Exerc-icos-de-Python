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
for C in range (len(text)):
    palavra = text[C]
    if palavra[0] in 'python':
        lista_nova.append(palavra)
    elif palavra[-1] in 'python':
        lista_nova.append(palavra)
print(f'Nova lista que tem "python": {lista_nova}')
