############# ordenaÃ§Ã£o ############
import random

def gera_numeros(tam):
    numeros = []
    for i in range(tam):
        numeros.append(random.randint(0,100))
    return numeros

#lista = gera_numeros(20)
lista = [65, 32, 61, 41, 87, 100, 19, 2, 1, 51, 92, 59, 25, 28, 55, 70, 14, 99, 6, 30]
lista2 = [65, 32, 61, 41, 87, 100, 19, 2, 1, 51, 92, 59, 25, 28, 55, 70, 14, 99, 6, 30]
#print(lista)
'''
[65, 32, 61, 41, 87, 100, 19, 2, 1, 51, 92, 59, 25, 28, 55, 70, 14, 99, 6, 30]
[]

[65, 32, 61, 41, 87, 100, 19, 2, 51, 92, 59, 25, 28, 55, 70, 14, 99, 6, 30]
[1]

[65, 32, 61, 41, 87, 100, 19, 51, 92, 59, 25, 28, 55, 70, 14, 99, 6, 30]
[1,2]

[65, 32, 61, 41, 87, 100, 19, 51, 92, 59, 25, 28, 55, 70, 14, 99, 30]
[1,2,6]

[65, 32, 61, 41, 87, 100, 19, 51, 92, 59, 25, 28, 55, 70, 99, 30]
[1,2,6,14]

[65, 32, 61, 41, 87, 100, 51, 92, 59, 25, 28, 55, 70, 99, 30]
[1,2,6,14,19]

[65, 32, 61, 41, 87, 100, 51, 92, 59, 28, 55, 70, 99, 30]
[1,2,6,14,19,25]

[65, 32, 61, 41, 87, 100, 51, 92, 59, 55, 70, 99, 30]
[1,2,6,14,19,25,28]
'''
def acha_menor(numeros):
    menor = numeros[0]
    for i in range(len(numeros)):
        if numeros[i] < menor:
            menor = numeros[i]
    return menor
def acha_maior(numeros):
    maior = numeros[0]
    for i in range(len(numeros)):
        if numeros[i] > maior:
            maior = numeros[i]
    return maior
def ordena_crescente(numeros):
    tam = len(numeros)
    ordenada = []
    for i in range(tam):
        #print(lista)
        #print(ordenada,'\n')
        menor = acha_menor(numeros)
        numeros.remove(menor)
        ordenada.append(menor)
    return ordenada
def ordena_decrescente(numeros):
    tam = len(numeros)
    ordenada = []
    for i in range(tam):
        #print(lista)
        #print(ordenada,'\n')
        maior = acha_maior(numeros)
        numeros.remove(maior)
        ordenada.append(maior)
    return ordenada

crescente = ordena_crescente(lista)
#print(lista)
#print(crescente,'\n')
decrescente = ordena_decrescente(crescente)
#print(decrescente)
lista2.sort()
#print(lista2)

#escreva um cÃ³digo que ordene a lista de forma decrescente
lista = [65, 32, 61, 41, 87, 100, 19, 2, 1, 51, 92, 59, 25, 28, 55, 70, 14, 99, 6, 30]
'''
primeiro passo
[65, 32, 61, 41, 87, 100, 19, 2, 1]
[32, 65, 61, 41, 87, 100, 19, 2, 1]
[32, 61, 65, 41, 87, 100, 19, 2, 1]
[32, 61, 41, 65, 87, 100, 19, 2, 1]
[32, 61, 41, 65, 87, 19, 100, 2, 1]
[32, 61, 41, 65, 87, 19, 2, 100, 1]
[32, 61, 41, 65, 87, 19, 2, 1, 100]

segundo passo
[32, 61, 41, 65, 87, 19, 2, 1, 100]
[32, 41, 61, 65, 87, 19, 2, 1, 100]
[32, 41, 61, 65, 19, 87, 2, 1, 100]
[32, 41, 61, 65, 19, 2, 87, 1, 100]
[32, 41, 61, 65, 19, 2, 1, 87, 100]

terceiro passo
[32, 41, 61, 65, 19, 2, 1, 87, 100]
[32, 41, 61, 19, 65, 2, 1, 87, 100]
[32, 41, 61, 19, 2, 65, 1, 87, 100]
[32, 41, 61, 19, 2, 1, 65, 87, 100]

quarto passo
[32, 41, 61, 19, 2, 1, 65, 87, 100]
[32, 41, 19, 61, 2, 1, 65, 87, 100]
[32, 41, 19, 2, 61, 1, 65, 87, 100]
[32, 41, 19, 2, 1, 61, 65, 87, 100]

quinto passo
[32, 41, 19, 2, 1, 61, 65, 87, 100]
[32, 19, 41, 2, 1, 61, 65, 87, 100]
[32, 19, 2, 41, 1, 61, 65, 87, 100]
[32, 19, 2, 1, 41, 61, 65, 87, 100]

sexto passo
[32, 19, 2, 1, 41, 61, 65, 87, 100]
[19, 32, 2, 1, 41, 61, 65, 87, 100]
[19, 2, 32, 1, 41, 61, 65, 87, 100]
[19, 2, 1, 32, 41, 61, 65, 87, 100]

sÃ©timo passo
[19, 2, 1, 32, 41, 61, 65, 87, 100]
[2, 19, 1, 32, 41, 61, 65, 87, 100]
[2, 1, 19, 32, 41, 61, 65, 87, 100]

oitavo psso
[2, 1, 19, 32, 41, 61, 65, 87, 100]
[1, 2, 19, 32, 41, 61, 65, 87, 100]
'''
lista = [65, 32, 61, 41, 87, 100, 19, 2, 1]
lista = gera_numeros(30)
print(lista)
num_while = 0
num_op = 0
while True:
    qtd_troca = 0
    num_op+=1
    for i in range(len(lista)-1-num_while):
        num_op+=1
        if lista[i] < lista[i+1]:
            qtd_troca+=1
            aux = lista[i]
            lista[i] = lista[i+1]
            lista[i+1] = aux
            print(lista)

    num_while+=1
    if qtd_troca==0:
        break
    print('\n')
print(num_op)
print(len(lista)**2)

print(f"foram realizdas {num_op/len(lista)**2}% das operaÃ§Ãµes")

with open("teste.txt",'r') as file:
    dados = file.readlines()
    for j in range(len(dados)):
        dados[j] = dados[j].replace(",",'')
        dados[j] = dados[j].replace('[','')
        dados[j] = dados[j].replace(']','')
        dados[j] = dados[j].split(" ")
        for i in range(len(dados[0])):
            dados[j][i] = int(dados[0][i])
        #print(dados[j])
        dados[j] = ordena_crescente(dados[j])
        #print(dados[j])
    print(dados[0])
    file.write("oi")
    #for linha in dados:
        #for elem in lista:
            #print(elem)
            #file.write(str(elem))