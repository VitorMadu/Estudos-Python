#listas: estrutura pra armazenar dados, variaveis etc. Admite qualquer tipo de dado
'''
lista = ["string",1,2.0,True]
print(lista)
lista = ["Danilo","rafa"]
print(lista)
lista.append("Gabi")
print(lista)
lista.remove("Danilo")
print(lista)
lista.pop()
print(lista)
'''
#fazer uma funÃ§Ã£o que recebe uma lista com nomes e retorna duas listas, uma somente com nomes de professores e outra somente com nomes de alunos
#Nomes de professor sÃ£o Danilo, Edson e Rafael
'''
def separa_prof_aluno(nomes):
    nomes_prof = []
    nomes_alunos = []

    for nome in nomes:
        print(nome)
        if nome == "Danilo":
            nomes_prof.append(nome)
        elif nome == "Rafael":
            nomes_prof.append(nome)
        elif nome == "Edson":
            nomes_prof.append(nome)
        else:
            nomes_alunos.append(nome)


    return [nomes_alunos,nomes_prof]
'''

def separa_prof_aluno(nomes,profs):
    nomes_prof = []
    nomes_alunos = []

    for nome in nomes:
        print(nome)
        if nome in profs:
            nomes_prof.append(nome)
        else:
            nomes_alunos.append(nome)


    return [nomes_alunos,nomes_prof]

def remove_aluno(nomes,nomes_de_professor):
    nomes_loop = nomes[:] #fazendo uma cÃ³pia da lista
    print(nomes_loop)
    for nome in nomes_loop:
        if nome not in nomes_de_professor:
            nomes.remove(nome)
    print(nomes)
    return

nomes = ["Danilo","Gabi","TaÃ­s","Rafael","Edson","Vinicius","Leticia","JoÃ£o","Felipe","Bruno","Victor"]
nomes_de_professor = ["Danilo","Edson","Rafael"]
#remove_aluno(nomes,nomes_de_professor)

#slicing [start:stop:step]: pegar subconjuntos da lista

#print(nomes[0:9:2])
nomes_novo = nomes[:]
for nome in nomes_novo:
#    print(nome)
    if nome in nomes_de_professor:
        nomes.remove(nome)
#print(nomes)



#alunos, professores = separa_prof_aluno(nomes,nomes_de_professor)
#print(alunos)
#print(professores)

#faÃ§am uma funÃ§Ã£o que receba uma lista com nomes e REMOVA nomes de professores
#faÃ§am uma funÃ§Ã£o ue receba uma lista com nomes e REMOVA nomes de alunos

nomes = ["Vinicius","Pedro","Lucas","OtÃ¡vio","Danilo","Edson","Rafael","Gabriela","Fernanda","FlÃ¡via"]

#for encadeado
lista_1 = [1,2,3,4,5,6,7,8,9,65,3,5,6,3,3,4]
lista_2 = [65,5,2,4,7,89]

#escrever uma funÃ§Ã£o que receba duas listas e nos dÃ¡ os elementos em COMUM Ã s listas
'''
lista_1[0]==lista_2[0], lista_2[1],lista_2[2]
lista_1[1]==lista_2[0], lista_2[1],lista_2[2]
lista_1[2]==lista_2[0], lista_2[1],lista_2[2]
.
.
.
lista_1[fim]==lista_2[0], lista_2[1],lista_2[2]
'''


def acha_comum(lista_1,lista_2):
    lista_em_comum = []
    for i in range(len(lista_1)):
        for j in range(len(lista_2)):
            if lista_1[i]==lista_2[j] and lista_1[i] not in lista_em_comum:
                lista_em_comum.append(lista_1[i])
    return lista_em_comum

#print(lista_em_comum)
#print(lista_1)
#print(lista_2)



#recebam duas listas com nÃºmeros e retorne uma lista SEM os elementos em comum Ã s listas

lista_diferentes = []
em_comum = acha_comum(lista_1,lista_2)

lista_1_diferente = []

for numero in lista_1:
    if numero not in em_comum:
        lista_1_diferente.append(numero)
#print(lista_1_diferente)
#print(lista_1)
#print(em_comum)
'''
for i in range(len(lista_1)):
    for j in range(len(lista_2)):
        if lista_1[i]!=lista_2[j] and lista_1[i] not in lista_diferentes:
            lista_diferentes.append(lista_1[i])
'''
#print(lista_diferentes)

matriz = [[1,2,3],[4,5,6],[7,8,9]]
#for i in range(3):
#    print(matriz[i])
#    for j in range(3):
#        print(matriz[i][j])
import matplotlib.pyplot as plt
import numpy as np


tamanho = 1000
matriz = np.zeros((tamanho,tamanho))
for i in range(tamanho):
    for j in range(tamanho):
        if i>=j:
            matriz[i][j] = 1
#print(matriz)
matriz= np.array(matriz)

########################## dicionÃ¡rios ################################

dicionario = {"chave" : "valor"}
dicionario = {"oi" : "olÃ¡", "tchau" : "atÃ© mais"}

#usuario = input("Diga oi : ")
#if usuario == "oi":
#    print("olÃ¡")
#elif usuario == "tchau":
#    print("atÃ© mais")

#resposta = dicionario[usuario]
#print(resposta)

dicionario = {"oi": ["olÃ¡","bom dia", "boa tarde"], "tchau" : ["atÃ© mais","flw","tmj"]}


usuario = input("Diga oi : ")
resposta = dicionario[usuario][0]
print(resposta)