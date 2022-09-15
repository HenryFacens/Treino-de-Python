#               1       2           3           4
# lista = ["chicago", "queens", "salvador", "pernambuco"]

# print(lista[1]) # printa o index [index]

# lista = ["chicago", "queens", "salvador", "pernambuco"]

# # print(lista[1:2]) # retorna o index ate o final que definirmos [1:2] = queens ate queens
# # print(lista[:3]) # chicago      queens      salvador
# print(lista[0:4:2]) # o [0:0:2] = pula o index de 2 em 2

# lista = ["chicago", "queens", "salvador", "pernambuco"]
# lista2 = ["pedreiro", "1021021"]
# lista += lista2

# print(len(lista)) #len é feito apra contagem de coisas dentro de um array ------------ # sum() = soma os elementos da listas # max() maior valor 
# print(max(lista)) # printa o oposto ===== min()
# caso print(list(range(10)))
 
# for x in range():
#     print(x,lista[x])

# lista = [""] #  []
# tupla = ("") # ()
# dicionario = {}

# dicionario = {"chave":"gab","chave3":"fuck","chave3":True}

# dicio = {
#     "nome":"Bruna",
#     "idade" : 27,
#     "nacionalidade" : "Brasieleira"

# }

# print(dicio["idade"])

# print(dicio.get("idade"))

# print(dicio.keys())

# print(len(dicio))

# print(dicio.values())

# dicio["valor"] = 32 # adiciona uma key valor com o o numero 32

# dicio.update = {"chave" : "valor"} #adicionar os valores

# dicio.pop("idade")

# print(dicio)

# del dicio["nome"]

# print(dicio)

# tulpla = ("item1","item2","item3")

# dicio = dict.fromkeys(tupla,tupla2)

#pode colocar um dicionario dentro de outro 

# dicionario = {
#     "dicionairo2": {
 
#         "dicionairo3": {

#             "nome" : "Clara",

#             "dicionario4": {


#             }
#         }
#     }


# }

# print(dicionario)
#print("item" in dicionario)
#set1.update #adiciona

# nome = "ana"

# def minha_funcao():
#     nome = "gabriel"
#     print(nome)
 

# minha_funcao()
# print(nome)

# def par_impar():
#     numero = 3
#     if (numero % 2) == 0:
#         return "numero par"
#     return"numero impar"

# print(par_impar())

# def olamundo():
#     print("ola mundo")

# def executar():
#     olamundo()

# executar()
# def funcao(nome): # Parametro e o nome dado aos valores utilizados
#     print(nome)
#     return 


# nome = input("qual o seu nome: ")
# funcao(nome)

# o * desempacota def fucao(*nome) --> salva em uma coisa só

# def imprimir_imovel(nomeImovel, n_quartos, vagas_garagem=None, *telefone)
# passa mais de um parametro no *telefone

# def imprimir_nomes(**nomes):
#     #print(nomes)
#     print(f"{nomes['nome']} {nomes['sobrenome']}")

# imprimir_nomes(nome="ana", sobrenome="julia")

# try except Exception as Err: print(Err)

# def reduzir_numeors(numeroint):
#     while numeroint > 0:
#         print(numeroint)
#         numeroint -=1


# while True:
#     print("-"*30)
#     try:
#         chamada = float(input('Coloque um valor numero: '))
#     except ValueError as Error:
#         Error = "Digite um numero"
#         print(Error)
#         continue

#     print("-"*30)
    
#     if chamada != 0 :
#         print("-"*30)
#         reduzir_numeors(chamada)
#         print("-"*30)
    
#     else:
#         break
 
# _init_-
# __name__
# __main__
# __doc__
# __file__
