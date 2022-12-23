# -*- coding: utf-8 -*-
"""1TDSPI_09_08.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1W6-GCBt8D1mmr7L9LjOt763mTdV4hK4L
"""

#fazer uma funÃ§Ã£o que recebe uma lista com nomes e remove os nomes de professores (Danilo, Edson, Ronqui)
nomes = ["Danilo","Edson","Ronqui","Vinicius","Gabi","Claudio","Pedro","Leticia","Alice","Maria"]
nomes_prof = ["Danilo","Edson","Ronqui"]

'''
def remove_professor(lista_nomes):

    lista = lista_nomes[:]
    for nome in lista:
        if nome == "Danilo":
            lista_nomes.remove(nome)
        elif nome ==  "Ronqui":
            lista_nomes.remove(nome)
        elif nome == "Edson":
            lista_nomes.remove(nome)
    return lista_nomes
'''

def remove_professor(lista_nomes,lista_profs):

    lista = lista_nomes[:]
    for nome in lista:
        if nome in lista_profs:
            lista_nomes.remove(nome)

    return lista_nomes

nomes_alunos = remove_professor(nomes,nomes_prof)
print(nomes_alunos)

#for encadeado
numeros_1 = [2,4,6,7,12,34,76,890,100]
numeros_2 = [2,42,61,7,12,37,71,890,1]
#encontrar elementos que pertenÃ§am Ã s duas listas (elementos em comum Ã s listas)

def acha_interseccao(numeros_1,numeros_2):
    lista_interseccao = []
    for i in range(len(numeros_1)):
        for j in range(len(numeros_2)):
          #print(i,'    ',j)
          if numeros_1[i] == numeros_2[j]:
              lista_interseccao.append(numeros_1[i])
    return lista_interseccao


def acha_diferente(numeros):
    lista_diferente = []
    lista_interseccao = acha_interseccao(numeros_1,numeros_2)
    for elemento in numeros:
        #passa por todos os elemento da numeros_1
        if elemento not in lista_interseccao:
            #pega somente elementos da numeros_1 que nao pertencem simultaneamente Ã  numero_2
            lista_diferente.append(elemento)
    return lista_diferente

lista_diferente_1 = acha_diferente(numeros_1)
lista_diferente_2 = acha_diferente(numeros_2)

print("NÃºmeros_1 : ",numeros_1)
print("NÃºmeros_2 : ",numeros_2)
print("Lista interseccao : ",lista_interseccao)
print("lista_diferente_1 : ",lista_diferente_1)
print("lista_diferente_1 : ",lista_diferente_2)


#encontrar uma lista com o que NÃƒO PERTENCE Ã€S DUAS LISTAS SIMULTANEAMENTE

################# Matrizes #####################

matriz = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]

#identifique a posiÃ§Ã£o do elemento 10 (linha, coluna)
for linha in range(3):
    for coluna in range(4):
       print(matriz[linha][coluna], end = " ")
       if matriz[linha][coluna] == 10 :
           print("\nlinha : ",linha, "coluna : ",coluna)
    print("\n")


import matplotlib.pyplot as plt
import numpy as np

plt.imshow(matriz)
