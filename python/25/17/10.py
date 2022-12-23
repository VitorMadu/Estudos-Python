import random
numeros = []
for i in range(10):
    numeros.append(random.randint(0,9))
#print(numeros)
'''
[5,3,1,7,8,9,1,2]
[1]

[5,3,7,8,9,1,2]
[1,1]

[5,3,7,8,9,2]
[1,1,2]

[5,3,7,8,9]
[1,1,2,3]

[5,7,8,9]
[1,1,2,3,5]

[7,8,9]
[1,1,2,3,5]

[7,9]
[1,1,2,3,5,7]

[9]
[1,1,2,3,5,7,8]

[]
[1,1,2,3,5,7,8,9]

numeros = [6, 3, 2, 9, 8, 9, 2, 7, 7, 8]

def acha_menor(lista_de_numeros):
    menor = lista_de_numeros[0]
    for i in range(len(lista_de_numeros)):
        if lista_de_numeros[i]<menor:
            menor = lista_de_numeros[i]
    return menor
def acha_maior(lista_de_numeros):
    maior = lista_de_numeros[0]
    for i in range(len(lista_de_numeros)):
        if lista_de_numeros[i]>maior:
            maior = lista_de_numeros[i]
    return maior

def acha_maior_menor(lista_de_numeros,condicao):
    menor = lista_de_numeros[0]
    maior = lista_de_numeros[0]
    for i in range(len(lista_de_numeros)):
        if lista_de_numeros[i]<menor:
            menor = lista_de_numeros[i]
        if lista_de_numeros[i]>maior:
            maior = lista_de_numeros[i]
    if condicao == 'menor':
        return menor
    elif condicao == 'maior':
        return maior

numeros = [6, 3, 2, 9, 8, 9, 2, 7, 7, 8]

def ordena_lista_crescente(lista_de_numeros):
    lista_ordenada = []
    for i in range(len(lista_de_numeros)):
        menor_elemeto = acha_maior_menor(lista_de_numeros,'menor')
        lista_ordenada.append(menor_elemeto)
        lista_de_numeros.remove(menor_elemeto)
    return lista_ordenada
def ordena_lista_decrescente(lista_de_numeros):
    lista_ordenada = []
    for i in range(len(lista_de_numeros)):
        maior_elemeto = acha_maior_menor(lista_de_numeros,'maior')
        lista_ordenada.append(maior_elemeto)
        lista_de_numeros.remove(maior_elemeto)
    return lista_ordenada

print(f"a lista original Ã© : {numeros}")
ordenada_crescente = ordena_lista_crescente(numeros)
print(f"a lista ordenada crescente com nosso mÃ©todo Ã© : {ordenada_crescente}")
ordenada_decrescente = ordena_lista_decrescente(ordenada_crescente)
print(f"a lista ordenada decrescente Ã© : {ordenada_decrescente}")
'''
######### bubble sort ############
'''
numeros = [6, 3, 2, 9, 8, 9, 2, 7, 7, 8]

[6, 3, 2, 9, 8, 9, 2, 7, 7, 8]
[3, 6, 2, 9, 8, 9, 2, 7, 7, 8]

[3, 2, 6, 9, 8, 9, 2, 7, 7, 8]

[3, 2, 6, 8, 9, 9, 2, 7, 7, 8]

[3, 2, 6, 8, 9, 2, 9, 7, 7, 8]

[3, 2, 6, 8, 9, 2, 7, 9, 7, 8]

[3, 2, 6, 8, 9, 2, 7, 7, 9, 8]

[3, 2, 6, 8, 9, 2, 7, 7, 8, 9]

###### segundo passo

[2, 3, 6, 8, 9, 2, 7, 7, 8, 9]

[2, 3, 6, 8, 2, 9, 7, 7, 8, 9]

[2, 3, 6, 8, 2, 7, 9, 7, 8, 9]

[2, 3, 6, 8, 2, 7, 7, 9, 8, 9]

[2, 3, 6, 8, 2, 7, 7, 8, 9, 9]

##### terceiro passo

[2, 3, 6, 8, 2, 7, 7, 8, 9, 9]

[2, 3, 6, 2, 8, 7, 7, 8, 9, 9]

[2, 3, 6, 2, 7, 8, 7, 8, 9, 9]

[2, 3, 6, 2, 7, 7, 8, 8, 9, 9]

##### terceiro passo

[2, 3, 6, 2, 7, 7, 8, 8, 9, 9]

[2, 3, 2, 6, 7, 7, 8, 8, 9, 9]

#### quarto passo

[2, 2, 3, 6, 7, 7, 8, 8, 9, 9]
'''
numeros = [6, 3, 2, 9, 8, 9, 2, 7, 7, 8]
print(numeros)
# len de numeros Ã© 10
#range(0,10-1)
def bubble_sort(lista_de_numeros):
    while True:
        qtd_trocas = 0
        for i in range(len(lista_de_numeros)-1):
            #print(f"{numeros[i]} comparado com {numeros[i+1]}")
            if lista_de_numeros[i]>lista_de_numeros[i+1]:
                aux = lista_de_numeros[i+1]
                lista_de_numeros[i+1] = lista_de_numeros[i]
                lista_de_numeros[i] = aux
                qtd_trocas+=1
                #print(qtd_trocas)
        if qtd_trocas==0:
            print(f"a lista ordenada Ã© {numeros}")
            break
    return lista_de_numeros
numeros = bubble_sort(numeros)
print(numeros)

############## arquivos ##############

file = open("teste.txt","w")
#file.write("deu certo de novo\n")
#file.write("deu certo de novo\n")
#file.write("deu certo de novo\n")
#file.write("deu certo de novo\n")
for j in range(10):
    numeros = []
    for i in range(10):
        numeros.append(random.randint(0,9))
    file.write(str(numeros)+'\n')