################# algoritmos de ordenaÃ§Ã£o #################
#import random
#numeros = []
#for i in range(10):
#    numeros.append(random.randint(0,20))
#print(numeros)

numeros = [9, 16, 2, 13, 12, 16, 7, 15, 15, 12]
#print(numeros,' ',set(numeros))
#numeros = [2, 7, 9 ,12, 12, 13, 15, 15, 16, 16]
#          [2, 7, 9, 12, 12, 13, 15, 15, 16, 16]
'''
def acha_menor(lista_de_numeros):
    if len(lista_de_numeros)>0:
        menor = lista_de_numeros[0]
    else:
        return
    for i in range(len(lista_de_numeros)):
        if lista_de_numeros[i]<menor:
            menor = lista_de_numeros[i]
    return menor

def meu_sort(lista_de_numeros):
    ordenada = []
    tam = len(lista_de_numeros)
    for i in range(tam):
        menor = acha_menor(lista_de_numeros)
        ordenada.append(menor)
        lista_de_numeros.remove(menor)
        print(ordenada,' ',lista_de_numeros)
    return ordenada

numeros = meu_sort(numeros)
print(numeros)
numeros2 = [9, 16, 2, 13, 12, 16, 7, 15, 15, 12]
numeros2.sort()
print(numeros2)

#crie uma funÃ§Ã£o que recebe uma lista e a ordena de forma decrescente
def acha_maior(lista_de_numeros):
    if len(lista_de_numeros)>0:
        maior = lista_de_numeros[0]
    else:
        return
    for i in range(len(lista_de_numeros)):
        if lista_de_numeros[i]>maior:
            maior = lista_de_numeros[i]
    return maior

def meu_sort_decrescente(lista_de_numeros):
    decrescente = []
    tam = len(lista_de_numeros)
    for i in range(tam):
        maior = acha_maior(lista_de_numeros)
        decrescente.append(maior)
        lista_de_numeros.remove(maior)
    return decrescente
print(meu_sort_decrescente(numeros2))
'''

############bubble sort############

'''
primeiro passo :

[9, 16, 2, 13, 12, 16, 7, 15, 15, 12]
[9, 2, 16, 13, 12, 16, 7, 15, 15, 12]
[9, 2, 16, 12, 13, 16, 7, 15, 15, 12]
[9, 2, 16, 12, 13, 7, 16, 15, 15, 12]
[9, 2, 16, 12, 13, 7, 15, 16, 15, 12]
[9, 2, 16, 12, 13, 7, 15, 15, 16, 12]
[9, 2, 16, 12, 13, 7, 15, 15, 12, 16]

segundo passo :
[2, 9, 16, 12, 13, 7, 15, 15, 12, 16]
[2, 9, 12, 16, 13, 7, 15, 15, 12, 16]
[2, 9, 12, 13, 16, 7, 15, 15, 12, 16]
[2, 9, 12, 13, 7, 16, 15, 15, 12, 16]
[2, 9, 12, 13, 7, 15, 16, 15, 12, 16]
[2, 9, 12, 13, 7, 15, 15, 16, 12, 16]
[2, 9, 12, 13, 7, 15, 15, 12, 16, 16]

terceiro passo:
[2, 9, 12, 7, 13, 15, 15, 12, 16, 16]
[2, 9, 12, 7, 13, 15, 12, 15, 16, 16]

quarto passo :
[2, 9, 7, 12, 13, 15, 12, 15, 16, 16]
[2, 9, 7, 12, 13, 12, 15, 15, 16, 16]

quinto passo :
[2, 7, 9, 12, 13, 12, 15, 15, 16, 16]
[2, 7, 9, 12, 12, 13, 15, 15, 16, 16]

sexto passo :
[2, 7, 9, 12, 12, 13, 15, 15, 16, 16]
'''

numeros = [9, 16, 2, 13, 12, 16, 7, 15, 15, 12]
def bubble_sort(lista_de_numeros):
    num_while = 0
    count = 0
    while True:
        qtd=0
        #print(lista_de_numeros,"\n\n")
        for i in range(len(lista_de_numeros)-1-num_while):
            anterior = lista_de_numeros[i]
            proximo = lista_de_numeros[i+1]
            if anterior > proximo:
                #print(f"vai trocar o {anterior} com o {proximo}")
                aux = anterior
                lista_de_numeros[i] = proximo
                lista_de_numeros[i+1] = aux
                qtd+=1
                #print(lista_de_numeros)
            count+=1
        num_while += 1
        if qtd==0:
            print(num_while*(len(lista_de_numeros)-1))
            print(count)
            print(num_while*(len(lista_de_numeros)-1)/count)
            return lista_de_numeros


import random
numeros = []
for i in range(100):
    numeros.append(random.randint(0,300))
print(numeros)
print(bubble_sort(numeros))

file = open("teste_1tdspi.txt","r")
#file.write("deu certo\ndeu certo\ndeu certo\ndeu certo\ndeu certo\ndeu certo\n")
#print(file.readlines())
seq = file.readlines()[0]
print(seq)
seq = seq.replace("\n",'')
seq = seq.split(",")
seq = [int(seq[i]) for i in range(len(seq))]
print(seq)
print(bubble_sort(seq))