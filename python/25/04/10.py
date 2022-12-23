############### dicionarios ###############
'''
dicionario = {"nome" : "Danilo"}
print(dicionario)
#print(dicionario["Danilo"])
dicionario["idade"] = [25]
print(dicionario)
dicionario["nome"] = ["Rafael"]
print(type(dicionario["nome"]))
#dicionario["nome"] = []
dicionario["nome"].append("Danilo")
print(dicionario)
dicionario["idade"].append(21)
print(dicionario)
print(dicionario["nome"][1])
print(dicionario.keys())
for key in dicionario.keys():
    print(key)
    print(dicionario[key])
    print(dicionario[key][1])

#crie um dicionario com as chaves int e float. Associe uma lista com 10 elementos int e 10 elementos float
#a cada chave
#printe todas as chaves presentes no dicionario
#printem o coneteudo de cada chave do dicionario
#printe somente os elementos INDICE par de cada chave

lista_inteiros = [1,2,3,4,5,6,7,8,9,0]
lista_float = [1.1,2.2,3.3,4.4,5.5,6.6,7.7,8.8,9.9,0.0]
numeros = {"int" : lista_inteiros, "float" : lista_float}
print(numeros)

numeros = {"int" : [], "float" : []}
for i in range(10):
    numeros["int"].append(i)
    numeros["float"].append(i/10)
print(numeros)

numeros = {}
print(numeros)
numeros["int"] = []
print(numeros)
numeros["float"] = []
print(numeros)
for i in range(10):
    numeros["int"].append(i)
    numeros["float"].append(i/10)
print(numeros)

numeros = {"int" : [], "float" : []}
for i in range(10):
    if i < 5:
        numeros["int"].append(i)
        numeros["float"].append(i/10)
    else:
        numeros["int"].append((i-4)*5)
        numeros["float"].append(i/10)

print(numeros)

'''

lista_inteiros = [1,2,3,4,5,6,7,8,9,0]
lista_float = [1.1,2.2,3.3,4.4,5.5,6.6,7.7,8.8,9.9,0.0]
numeros = {"int" : lista_inteiros, "float" : lista_float}
print(numeros)
'''
for key in numeros.keys():
    print(key)

print(numeros.values())
for value in numeros.values():
    print(value)

for key in numeros.keys():
    print(numeros[key])

#print(type(numeros["int"]))
#print(numeros["int"][4])
#print("\n\n")
for i in range(10):
    if i%2==0:
        print(numeros["int"][i])
'''
for key in numeros.keys():
    for i in range(len(numeros[key])):
        #print(key,len(numeros[key]))
        if i%2==0:
            print(numeros[key][i],end = " ")
    print("\n")

#crie dois dicionarios de carros contendo as chaves nome, ano e preÃ§o. Preencha cada chave com 5 valores
#crie um terceiro dicionario com a uniÃ£o de todos os valores

carros1 = {"nome" : ["fusca","kombi","brasÃ­lia","chevete","ka"],
           "ano" : [2001,2002,2003,2004,2005],
           "preÃ§o" : [150,20,300,411,502]}

carros2 = {"nome" : ["tucson","renegade","sonata","x6","golf"],
           "ano" : [2011,2012,2013,2014,2015],
           "preÃ§o" : [106,2000,30,400,50000],
           "portas" : [2,4,2,2,4]}
carros3 = {}
for key in carros1.keys():
    if key in carros2.keys():
        carros3[key] = carros1[key] + carros2[key]
print(carros3)
#import pandas as pd
#carros3 = pd.DataFrame(carros3)
#busque o carro mais barato e me fale o seu nome
indice_menor = 0
menor = carros3["preÃ§o"][indice_menor]

for i in range(len(carros3["preÃ§o"])):
    if carros3["preÃ§o"][i] < menor:
        menor = carros3["preÃ§o"][i]
        indice_menor = i
print(carros3["nome"][indice_menor])