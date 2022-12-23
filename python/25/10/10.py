############## dicionarios ##############
'''
alunos = {"nome" : "Danilo"}
print(alunos["nome"])
print(alunos)
#print(alunos["Danilo"])
alunos["idade"] = 25
print(alunos)
alunos["nome"] = "Vinicius"
print(alunos)
alunos["nome"] = ["Vinicius"] #agora alunos["nome"] Ã‰ uma lista
print(alunos)
print(alunos["nome"])
print(alunos["nome"][0])
alunos["nome"].append("Danilo")
print(alunos["nome"])
alunos["idade"] = [alunos["idade"]]
print(alunos["idade"])
alunos["idade"].append(17)
print(alunos["idade"])
print(alunos["idade"][0])
print(alunos["idade"][1])
#print(alunos["idade"][2])

alunos = {"nome" : ["Danilo","Vinicius"], "idade" : [25,17]}
print(alunos.keys())
for chave in alunos.keys():
    print(chave)

for chave in alunos.keys():
    print(alunos[chave])

#crie um dicionario com a chave par e preencha com os 10 primeiros numeros pares
#nesse mesmo dicioario crie uma nova chave impar e preencha com os 10 primeiros impares
#encontre a media dos elementos de cada chave (soma de todos os elementos dividido pela qtd de elementos)
#encontre o maior/menor numero de cada chave

numeros = {"par" : []}
#numeros["par] Ã© a lista vazia, tem len 0
i=0
while len(numeros["par"])<10:
    if i%2==0:
        numeros["par"].append(i)
    print(numeros["par"])
    i+=1
print(numeros)
numeros = {"par" : []}
for i in range(0,20,2):
    numeros["par"].append(i)
#print(numeros)

numeros["impar"] = []
#print(numeros)
for i in range(1,20,2):
    numeros["impar"].append(i)
#print(numeros)

#print(numeros["par"][9])
#for i in range(len(numeros["par"])):
#    print(numeros["par"][i])

#for key in numeros.keys():
#    for i in range(len(numeros[key])):
#        print(numeros[key][i])

lista = [1,2,3,4,5]
soma = 0
for elem in lista:
    soma+=elem
    #print(soma)

for key in numeros.keys():
    soma = 0
    for elem in numeros[key]:
        soma += elem
    #print(f"A mÃ©dia dos elementos na chave {key} Ã© {soma/len(numeros[key])}")

#lista = [6,2,4,5,1,7,9]
#menor = lista[0]
#for elem in lista:
#    print(f"aqui comparamos {elem} com {menor}")
#    if elem<menor:
#        menor = elem
#print(f"o menor elemento Ã© {menor}")

for key in numeros.keys():
    menor = numeros[key][0]
    maior = numeros[key][0]
    for elem in numeros[key]:
        if elem < menor:
            menor = elem
        if elem > maior:
            maior = elem
    #print(f"o menor elemento da lista na chave {key} Ã© {menor} e o maior Ã© {maior}")

#crie dois dicionarios com as chaves nomes e idades, preencha com listas de nomes e idades
#crie um terceiro que verifica se ha chaves em comum, e se houver una os conteudos das chaves equivalentes


pessoas1 = {}
pessoas1["nomes"] = ["Danilo","Victor","Rafaela"]
#print(pessoas1)
pessoas1["idades"] = [25,22,18]
#print(pessoas1)

pessoas2 = {"nomes" : [], "idades" : []}
pessoas2["nomes"].append("Vinicius")
pessoas2["nomes"].append("Gabriela")
pessoas2["nomes"].append("Rafael")
#print(pessoas2)
pessoas2["idades"].append(21)
pessoas2["idades"].append(25)
pessoas2["idades"].append(19)
#print(pessoas2)

pessoas3 = {}
for key in pessoas1.keys():
    if key in pessoas2.keys():
        pessoas3[key] = pessoas1[key]+pessoas2[key]
        #print(f"pessoas 3 Ã© {pessoas3}")

#me diga o nome da pessoa mais nova em pessoas3

def acha_menor(lista):
    indice_menor = 0
    menor = lista[indice_menor]
    for i in range(len(lista)):
        if lista[i] < menor:
            menor = lista[i]
            indice_menor = i
    return menor,indice_menor

menor_idade, indice_menor_idade = acha_menor(pessoas3["idades"])
#print(f"a menor idade Ã© {menor_idade} e estÃ¡ no indice {indice_menor_idade}")
#print(f"a pessoa mais nova Ã© o/a {pessoas3['nomes'][indice_menor_idade]} e ela tem {menor_idade} anos")

frase = "O sabiÃ¡ nÃ£o sabia que o sÃ¡bio sabia que o sabiÃ¡ nÃ£o sabia assobiar."
#escreva um cÃ³digo que recebe uma frase e conta quantas vezes cada palavra aparece nela.
#armazene isso em um dicionario

# dic = {"o": 3, "sabiÃ¡" : 2, "nÃ£o" : 2, "sabia" : 3,"que" : 2, "sÃ¡bio": 1,"assobiar": 1}
#       {'o': 3, 'sabiÃ¡': 2, 'nÃ£o': 2, 'sabia': 3, 'que': 2, 'sÃ¡bio': 1, 'assobiar': 1}
print(frase)
frase = frase.lower()
print(frase)
frase = frase.replace('.','')
print(frase)
frase = frase.split(" ")
print(frase)

palavras = {}
for palavra in frase:
    if palavra in palavras.keys():
        palavras[palavra] +=1
    else:
        palavras[palavra] = 1
    print(palavras)

import pandas as pd
dados = pd.read_csv('dado_mg.csv')
print(dados)
#dados = pd.read_csv('dado_mg.csv',sep=";")
#print(dados)
colunas = str(dados.columns[0])
print(colunas)
colunas = colunas.split(";")
print(colunas)
dado1 = dados[dados.columns[0]][0]
dado1 = dado1.split(";")
print(dado1)

dicionario = {}
for i in range(len(colunas)):
    nova_chave = colunas[i]
    novo_valor = dado1[i]
    dicionario[nova_chave] = [dado1[i]]
print(dicionario)
#print("\n")
#dicionario = pd.DataFrame(dicionario)
#print(dicionario)

for i in range(1,len(dados)):
    #print(f"estamos no dado {i}")
    dado = dados[dados.columns[0]][i]
    dado = dado.split(";")
    for j in range(len(dado)):
        chave = colunas[j]
        dicionario[chave].append(dado[j])
#print(dicionario)
print("\n")
dicionario = pd.DataFrame(dicionario)
print(dicionario)
'''

def acha_menor(lista):
    if lista!=[]:
        menor = lista[0]
    else:
        return
    for elem in lista:
        if elem<menor:
            menor=elem
    return menor

numeros = [7,7,4,4,2,5,1,4,8,9,10,11,19] #[1,2,4,5,7,8,9,10,11,19]
                                   #[1,2,4,5,7,8,9,10,11,19]
qtd = len(numeros)
numeros_ordenada = []
while len(numeros_ordenada)!=qtd:
     menor = acha_menor(numeros)
     numeros_ordenada.append(menor)
     numeros.remove(menor)
#     print(numeros_ordenada,' ',numeros)

#print(acha_menor(numeros))


numeros = [7,4,2,5,1,8,9,10,11,19]
#numeros = [4,7,2,5,1,8,9,10,11,19]
#numeros = [4,2,7,5,1,8,9,10,11,19]
#numeros = [4,2,5,7,1,8,9,10,11,19]
#numeros = [4,2,5,1,7,8,9,10,11,19]

#numeros = [2,4,5,1,7,8,9,10,11,19]
#numeros = [2,4,1,5,7,8,9,10,11,19]

#numeros = [2,1,4,5,7,8,9,10,11,19]

#numeros = [1,2,4,5,7,8,9,10,11,19]

#bubble sort
numeros = [7,4,2,5,1,8,9,10,11,19]

while True:
    qtd = 0
    for i in range(len(numeros)-1):
        if numeros[i]>numeros[i+1]:
            temp = numeros[i]
            numeros[i] = numeros[i+1]
            numeros[i+1] = temp
            qtd+=1
        print(numeros)
    if qtd==0:
        break

