############# funÃ§oes e listas ##############



def par_impar(lista_numeros):
    par_ou_impar = []
    for num in lista_numeros:
        if num%2==0:
            par_ou_impar.append("par")
        else:
            par_ou_impar.append("impar")
    return par_ou_impar
numero = [10,2,5,7,8,9]
resultado = par_impar(numero)
#print(resultado)
outra_lista = [12,13,3,4,67,68]
resultado = par_impar(outra_lista)
#print(resultado)

#fatorial de 10: 10! = 1*2*3*4...*9*10



def fatorial(numero):
    fat = 1
    for i in range(1,numero+1):
        #print(fat,i)
        fat*=i
    return fat

numero = 10
fato = fatorial(numero)
#print(fato)

#verificaÃ§Ã£o de numero primo

#7%1==0
#7%2==1
#7%3==1
#7%4==3
#7%5==2
#7%6==1
#7%7==0

#15%2==1
#15%3==0


def checa_primo(numero):
    for i in range(2,numero):
        if numero%i==0:
            #print(i)
            resposta = False
            break
        elif i==numero-1:
            resposta = True
    return resposta




resultado = checa_primo(numero)
#print(resultado)

def primos(lista_numeros):
    lista_primos=[]
    for num in lista_numeros:
        if checa_primo(num):
            lista_primos.append(True)
        else:
            lista_primos.append(False)
    return lista_primos

numeros = [15,13,11,23,21,7]
#print(numeros)
lista_primos = primos([3,4])
#print(lista_primos)


#1- Escreva uma funÃ§Ã£o que "planifica" uma lista de listas.
# Original: [0, 10, [20, 30], 40, 50, [60, 70, 80], [90, 100, 110, 120]]
# Planficada: [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120]
lista = [0,1,[1,2,3,4]]
def planifica_lista(lista):
    nova_lista = []
    for num in lista:
        if type(num) is list:
            for i in num:
                nova_lista.append(i)
        else:
            nova_lista.append(num)
    return nova_lista
#print(lista)
planificada = planifica_lista(lista)
#print(planificada)


original = [0, 10, [20, 30], 40, 50, [60, 70, 80], [90, 100, 110, 120]]
planficada = planifica_lista(original)
#print(original)
#print(planficada)

#4- Escreva uma funÃ§ao que acha o maximo e o minimo valor numÃ©rico de uma lista heterogenea
# valores mÃ¡ximo e mÃ­nimo: [5, 2]

def filtra_numeros(lista):
    original_numerica = []
    for elem in lista:
        if type(elem) is int:
            original_numerica.append(elem)
    return original_numerica

def maior_menor(lista_de_numeros):
    #print(lista_de_numeros)
    lista_de_numeros = filtra_numeros(lista_de_numeros)
    #print(lista_de_numeros)
    menor = lista_de_numeros[0]
    maior = lista_de_numeros[0]
    for num in lista_de_numeros:
        if num < menor:
            menor = num
        if num > maior:
            maior = num
    return [maior,menor]

original = ['Python', 3, 2, 4, 5, 'version']
maior, menor = maior_menor(original)
#print("maior : ",maior)
#print("menor : ",menor)
#print(original)
#original = filtra_numeros(original)
#print(original)


#6- Escreva uma funÃ§Ã£o que encontra o numero de elementos inteiros pertencentes a uma lista
#Original: [1, 'abcd', 3, 1.2, 4, 'xyz', 5, 'pqr', 7, -5, -12.22]
#Numero de inteiros: 6
def conta_inteiros(lista):
    count = 0
    for elem in lista:
        if type(elem) is int:
            count +=1
    return count
original = [1, 'abcd', 3, 1.2, 4, 'xyz', 5, 'pqr', 7, -5, -12.22]
numero_de_inteiros = conta_inteiros(original)
#print(numero_de_inteiros)
numero_de_inteiros = conta_inteiros([1,2.3,4,5,"lista"])
#print(numero_de_inteiros)

#8- Escreva uma funÃ§Ã£o para encontrar elementos em comum numa lista de listas. Por
#exemplo, nessa lista contendo 3 listas cada uma tem os elementos 12 e 18.
#Original: [[12, 18, 23, 25, 45], [7, 12, 18, 24, 28], [1, 5, 8, 12, 15, 16, 18]]
#Elementos em comum: [18, 12]

original = [[12, 18, 23, 25, 45], [7, 12, 18, 24, 28], [1, 5, 8, 12, 15, 16, 18]]
print(len(original))
print(len(original[0]))
print(12 in original[0] and 12 in original[1] and 12 in original[2])





