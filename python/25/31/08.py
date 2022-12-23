############## exercÃ­cios ##################

def par_ou_impar(lista_numeros):
    resultado=[]
    for num in lista_numeros:
        if num%2==0:
            resultado.append("Ã© par")
        else:
            resultado.append("Ã© Ã­mpar")
    return resultado

numeros = [4,3,2,4,5,7,2,4,6]
#resposta = par_ou_impar([3,3,3,3])
#print(resposta)

################### fatorial #############
#faÃ§a uma funÃ§Ã£o que acha o fatorial de um nÃºmero
#5! = 1*2*3*4*5
numeros = [4,3,2,4,5,7,2,4,6]

def fatorial(lista_numero):
    lista_fatorial = []
    for num in lista_numero:
        fat = 1
        for i in range(2,num+1):
            fat*=i
        lista_fatorial.append(fat)
    return lista_fatorial
#print(fatorial(numeros))

def acha_media(lista_numeros):
    soma=0
    for num in lista_numeros:
        soma+=num
    media = soma/len(numeros)
    return media

def desvio_padrao(lista_numeros):
    subtracao = []
    media = acha_media(lista_numeros)
    for num in lista_numeros:
        sub = (num - media)**2
        subtracao.append(sub)
    soma = 0
    for elem in subtracao:
        soma+=elem
    soma/=len(lista_numeros)
    soma = soma**0.5
    return soma
#print(desvio_padrao(numeros))
#print(numeros)


#8- Escreva uma funÃ§Ã£o para enontrar elementos em comum numa lista de listas. Por
#exemplo, nessa lista contendo 3 listas cada uma tem os elementos 12 e 18.
#Original:
#[[12, 18, 23, 25, 45], [7, 12, 18, 24, 28], [1, 5, 8, 12, 15, 16, 18]]
#Elementos em comum:
#[18, 12]

lista = [[12, 18, 23, 25, 45], [7, 12, 18, 24, 28], [1, 5, 8, 12, 15, 16, 18]]
print(len(lista))
print(lista[0])
print(17 in lista[1] and 12 in lista[2])

#lista_comum =[]
#for elem in lista[0]:
#    if elem in lista[1] and elem in lista[2]:
#        lista_comum.append(elem)
#print(lista_comum)


#lista_comum =[]
#for elem in lista[0]:
#    if elem in lista[1]:
#        if elem in lista[2]:
#            lista_comum.append(elem)
#print(lista_comum)

def acha_comum(lista):
    lista_comum =[]
    for elem in lista[0]:
        for i in range(1,len(lista)-1):
            if elem not in lista[i]:
                break
            if i == len(lista)-2:
                lista_comum.append(elem)
    return lista_comum
print(acha_comum(lista))


#5- Escreva uma funÃ§ao que acha a diferenÃ§a entre numeros consecutivos numa lista;
#Original:
#[1, 1, 3, 4, 4, 5, 6, 7]
#diferenÃ§a:
#[0, 2, 1, 0, 1, 1, 1]



def subtrai(lista):
    lista_sub = []
    for i in range(len(lista)-1):
         lista_sub.append(lista[i+1]-lista[i])
    return lista_sub
print(subtrai([1, 1, 3, 4, 4, 5, 6, 7]))

