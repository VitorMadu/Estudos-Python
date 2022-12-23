#1 - Preencher uma lista com 10 elementos float
#2 - funÃ§Ã£o para somar os elementos da lista
#3 - funÃ§Ã£o para calcular a mÃ©dia dos elementos
#4 - funÃ§Ã£o que retorna uma lista com os elementos acima da media
#5 - funÃ§Ã£o que retorna o maior e o menor elemento da lista
#7 - funÃ§Ã£o que retorna somente os elementos negativos
#8 - Guardar numa lista True or false caso o elemento esteja acima/abaixo da mÃ©dia

#from random import randint
#lista = []
#for i in range(10):
#    lista.append(float(randint(-10,10)))


lista = [-1.0, -9.0, -5.0, 8.0, -8.0, -4.0, 4.0, -1.0, 6.0, 9.0]
print(lista)
def soma(numeros):
    sum = 0
    for num in numeros:
        sum +=num
    return sum
soma_lista = soma(lista)

def media(numeros):
    soma_numeros = soma(numeros)
    media_numeros = soma_numeros/len(numeros)
    return media_numeros
print("a mÃ©dia Ã© : ",media(lista))

def acima_media(numeros):
    media_numeros = media(numeros)
    acima_da_media = []
    for num in numeros:
        if num>media_numeros:
            acima_da_media.append(num)
    return acima_da_media
print("acima da media : ", acima_media(lista))

def min_max(numeros):
    min = numeros[0]
    max = numeros[0]
    for num in numeros:
        if num < min:
            min = num
        if num > max:
            max = num
    return [min,max]

minimo,maximo = min_max(lista)
print(f"o minimo Ã© {minimo} e o maximo Ã© {maximo}")

def acha_neg(numeros):
    lista_neg = []
    for num in numeros:
        if num <0:
            lista_neg.append(num)
    return lista_neg

print(acha_neg(lista))

def acima_media_bool(numeros):
    ac_media = acima_media(numeros)
    ac_media_bool = []
    for num in numeros:
        if num in ac_media:
            ac_media_bool.append(True)
        else:
            ac_media_bool.append(False)
    return ac_media_bool
print("True Ã© acima False Ã© abaixo : ",acima_media_bool(lista))