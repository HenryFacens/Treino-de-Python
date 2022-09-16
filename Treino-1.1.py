# '''Manipulacao de arquivo'''
# with open('receita.txt') as arquivo:
#     print(arquivo.read())
#     print(arquivo.closed)
# print(arquivo.closed)

# '''
# 'r' 'a' 'w'
# '''



# with open('receita.txt','a') as arquivo:
#     arquivo.write('Imaginacao')

from pydf import generate_pdf

pdf = generate_pdf('<h1>this is html</h1>')

with open('meuarquivo.pdf','wb') as arquivo:
    arquivo.write(pdf)