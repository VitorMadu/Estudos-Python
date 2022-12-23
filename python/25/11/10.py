'''
dicionario = {"nome" : "Danilo"}
print(dicionario["nome"])
print(dicionario)
#print(dicionario["Danilo"])
dicionario["idade"] = 25
print(dicionario)
dicionario["nome"] = "claudio"
print(dicionario)
dicionario["nome"] = [dicionario["nome"]]
print(dicionario)
dicionario["idade"] = [dicionario["idade"]]
print(dicionario)
#dicionario["nome"] representa uma lista
print(type(dicionario["idade"]))
dicionario["nome"].append("Danilo")
dicionario["idade"].append(23)
print(dicionario)
print(dicionario["nome"][0])
dicionario["curso"] = "TDS"
print(dicionario)
#dic = {"endereÃ§o" : {"rua" : "9 de julho", "numero" : 72}, "filhos" : ["gabriel","gabriela"]}
#print(dic["endereÃ§o"].keys())
print(dicionario.keys())
for key in dicionario.keys():
    print(key)
    if type(dicionario[key]) is list:
        print(dicionario[key][0])

#criem dois dicionarios com 3 chaves cada, 2 em comum.
# dic1 = {int : [1,2,3],float : [1.2], string : ["a","b","c"]}
# dic2 = {int : [4,5,6],bool : [True], string : ["d","e","f"]}
# dic3 = {"int" : [1,2,3,4,5,6],"string" : ["a","b","c","d","e","f"]}
# verifique se hÃ¡ chaves em comum aos dois dicionarios e crie um terceiro dicionario com a
# uniao dos conteudos dessas chaves
dic1 = {"int" : [1,2,3],"float" : [1.2], "string" : ["a","b","c"]}
dic2 = {"int" : [4,5,6],"bool" : [True], "string" : ["d","e","f"]}

dic3 = {}
for key1 in dic1.keys():
    print(key1," ", dic2.keys())
    if key1 in dic2.keys():
        dic3[key1] = dic1[key1] + dic2[key1]
    print("dic3 keys : ",dic3.keys())
print(dic3)

#conte quantas vezes cada palavra aparece na frase
frase = "O sabiÃ¡ nÃ£o sabia que o sÃ¡bio sabia que o sabiÃ¡ nÃ£o sabia assobiar."
#palavras = {"o":3,"sabiÃ¡" :2,"nÃ£o" : 2, "sabia" : 3, "que" : 2, "sÃ¡bio" : 1,"assobiar" : 1}
print(frase)
frase = frase.lower()
print(frase)
frase = frase.replace(".",'')
print(frase)
frase = frase.split(" ")
print(frase)
palavras = {}
for palavra in frase:
    if palavra not in palavras.keys():
        palavras[palavra] = 1
    else:
        palavras[palavra] += 1
    print(palavra," ",palavras)

#criem um dicionario com nomes de carros, ano de fabricaÃ§Ã£o e preÃ§o e me traga todas as informaÃ§Ãµes
#a respeito do carro mais barato

carros = {"modelo": ["Fusca", "Golf", "Gol","brasÃ­lia","ka"],
          "preco": [10000,50000,35000,1000,2000],
          "fabricacao": [1995, 2013, 2006,1960,2010]}

indice_menor = 0
menor = carros["preco"][indice_menor]
for i in range(len(carros["preco"])):
    valor = carros["preco"][i]
    print(valor," ",menor)
    if valor<menor:
        menor = valor
        indice_menor = i

print(f"O carro {carros['modelo'][indice_menor]} Ã© o mais barato, vale R${menor} e foi fabricado em {carros['fabricacao'][indice_menor]}")


print(menor," ",indice_menor)
############################################################################################
'''
import pandas as pd
dados = pd.read_csv("dado_mg.csv")
print(dados)