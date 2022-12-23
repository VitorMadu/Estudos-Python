############### ordenaÃ§Ã£o ################

import random


#tam = 10
#numeros = []
#for i in range(tam):
#    numeros.append(random.randint(0,100))
#print(numeros)

#numero = [31, 86, 15, 22, 55, 87, 31, 49, 39, 63]
#numero2 = [31, 86, 15, 22, 55, 87, 31, 49, 39, 63]
'''
[31, 86, 15, 22, 55, 87, 31, 49, 39, 63]
[]

[31, 86, 22, 55, 87, 31, 49, 39, 63]
[15]

[31, 86, 55, 87, 31, 49, 39, 63]
[15, 22]

[86, 55, 87, 31, 49, 39, 63]
[15, 22, 31]

[86, 55, 87, 49, 39, 63]
[15, 22, 31, 31]

[86, 55, 87, 49, 63]
[15, 22, 31, 31, 39]

[86, 55, 87, 63]
[15, 22, 31, 31, 39, 49]

[86, 87, 63]
[15, 22, 31, 31, 39, 49, 55]

[86, 87]
[15, 22, 31, 31, 39, 49, 55, 63]

[87]
[15, 22, 31, 31, 39, 49, 55, 63, 86]

[]
[15, 22, 31, 31, 39, 49, 55, 63, 86, 87]
'''
def acha_menor(numeros):
    menor = numeros[0]
    for num in numeros:
        if num<menor:
            menor = num
    return menor

def acha_maior(numeros):
    maior = numeros[0]
    for num in numeros:
        if num>maior:
            maior = num
    return maior


def ordena_decrescente(numeros):
    tam = len(numeros)
    ordenada = []
    for i in range(tam):
        #print(numeros)
        #print(ordenada)
        #print('\n')
        maior = acha_maior(numeros)
        numeros.remove(maior)
        ordenada.append(maior)
    return ordenada




def ordena_crescente(numeros):
    tam = len(numeros)
    ordenada = []
    for i in range(tam):
        print(numeros)
        print(ordenada)
        print('\n')
        menor = acha_menor(numeros)
        numeros.remove(menor)
        ordenada.append(menor)
    return ordenada
#numero = ordena_crescente(numero)

#print(numero)
#numero2.sort()
#print(numero2)
#numero = ordena_decrescente(numero)
#print(numero)
#print(ordenada)

#faÃ§a um algoritmo que ordene de forma decrescente


#teste = [15, 22, 31, 31, 39, 49, 55, 63, 86, 87]
#teste = ordena_crescente(teste)

#ordena crescente faz ~ nÂ² operaÃ§Ãµes
'''
[31, 86, 15, 22, 55, 87, 31, 49, 39, 63]
[31, 15, 86, 22, 55, 87, 31, 49, 39, 63]
[31, 15, 22, 86, 55, 87, 31, 49, 39, 63]
[31, 15, 22, 55, 86, 87, 31, 49, 39, 63]
[31, 15, 22, 55, 86, 31, 87, 49, 39, 63]
[31, 15, 22, 55, 86, 31, 49, 87, 39, 63]
[31, 15, 22, 55, 86, 31, 49, 39, 87, 63]
[31, 15, 22, 55, 86, 31, 49, 39, 63, 87]

[15, 31, 22, 55, 86, 31, 49, 39, 63, 87]
[15, 22, 31, 55, 86, 31, 49, 39, 63, 87]
[15, 22, 31, 55, 31, 86, 49, 39, 63, 87]
[15, 22, 31, 55, 31, 49, 86, 39, 63, 87]
[15, 22, 31, 55, 31, 49, 39, 86, 63, 87]
[15, 22, 31, 55, 31, 49, 39, 63, 86, 87]

[15, 22, 31, 55, 31, 49, 39, 63, 86, 87]
[15, 22, 31, 31, 55, 49, 39, 63, 86, 87]
[15, 22, 31, 31, 49, 55, 39, 63, 86, 87]
[15, 22, 31, 31, 49, 39, 55, 63, 86, 87]

[15, 22, 31, 31, 49, 39, 55, 63, 86, 87]
[15, 22, 31, 31, 39, 49, 55, 63, 86, 87]

[15, 22, 31, 31, 39, 49, 55, 63, 86, 87]
'''


def bubble_sort(lista):
    qtd_operacoes = 0
    num_while = 0
    while True:
        qtd = 0
        qtd_operacoes +=1
        for i in range(len(lista)-1-num_while):
            qtd_operacoes+=1
            if lista[i] > lista[i+1]:
                qtd+=1
                aux = lista[i]
                lista[i] = lista[i+1]
                lista[i+1] = aux
                #print(lista)

        #print("\n")
        num_while+=1
        if qtd == 0:
            #print("A QTD OPERACOES FOI : ",qtd_operacoes)
            return lista
tam = 10
teste = []
for i in range(tam):
    teste.append(random.randint(0,100))

#teste = [31, 86, 15, 22, 55, 87, 31, 49, 39, 63]
#teste = bubble_sort(teste)
#print(teste)

#file = open("teste.txt",'r+')

# with open("teste.txt",'r+') as file:
#     dados = file.readlines()
#     print(dados[0].split(" "))
#     for j in range(len(dados)):
#         dados[j] = dados[j].split(" ")
#         print(dados[j])
#         for i in range(len(dados[0])):
#             dados[j][i] = int(dados[j][i])
#     print(dados)
#     for i in range(len(dados)):
#         dados[i] = bubble_sort(dados[i])
#     print(dados)
#     file.write("\n")
#     for linha in dados:
#         file.write(str(linha).replace(",",'').replace("[",'').replace("]",''))
#         file.write("\n")
#

    #for i in range(len(dados[0])):
        #print(int(dados[0][i]))
        #dados[0][i] = int(dados[0][i])
    #print(dados[0])