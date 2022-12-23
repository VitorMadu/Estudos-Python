################### funÃ§Ãµes ###################

'''
def eh_par(num):
    if num%2==0:
        resposta = "Ã© par"
    else:
        resposta = "Ã© impar"
    return resposta

while True:
    s_ou_n = input("digite sim se quer digitar numeros ou nao se quiser parar : ")
    if s_ou_n == "sim":
        num = int(input("Digite um numero : "))
        par_ou_impar = eh_par(num)
        print(par_ou_impar)
    else:
        print("flw")
        break
'''
# faÃ§a uma funÃ§Ã£o que receba uma lista de nÃºmeros e retorne quais deles sÃ£o primos
# numeros primos sÃ£o aquele que sÃ³ sÃ£o divisiveis por 1 e por ele mesmo

#numeros = [1,2,3,4,5,6,7,8,9,10,11] #resposta = [1,2,3,5,7,11]

#num%2==0
#num%3==0
#num%4==0
#...
#num%num-1==0

def eh_primo(numeros):
    primos = []
    for num in numeros:
        #print(num)
        for i in range(1,num):
            print(i)
            if num%i==0 and i!=1:
                break
            elif i == num-1:
                primos.append(num)
    return primos

#numeros = [1,2,3,4,5,6,7,8,9,10,11]
#primo = eh_primo(numeros)
#print(primo)

#import math
from math import sqrt
#print(sqrt(8.4))
#print(8.4**0.5)
#fazer uma funÃ§Ã£o que recebe uma lista de nÃºmeros e retorna a raiz quadrada dos nÃºmeros na lista

def raiz(numeros):
    raizes = []
    for num in numeros:
        if num>0:
            raizes.append(sqrt(num))
    return raizes

numeros = [1,2,3,-4,5,6,7,8,9,10,11]
raizes = raiz(numeros)
#print(raizes)

#escreva um cÃ³digo que recebe a, b e c de uma eq de segundo grau e retorna os valores de x possÃ­veis

def acha_delta(a,b,c):
    delta = b**2 - 4*a*c
    return delta
def resolve_equacao(a,b,c):
    delta = acha_delta(a,b,c)
    if delta>=0:
        x1 = (-b+sqrt(delta))/(2*a)
        x2 = (-b-sqrt(delta))/(2*a)
        return [x1,x2]
    else:
        resposta = "erro, delta negativo"
        return resposta

'''
while True:
    s_ou_n = input("voce quer encontrar raizes de equaÃ§Ãµes de segundo grau ?")
    if s_ou_n == "sim":
        a = float(input("Digite o a : "))
        b = float(input("Digite o b : "))
        c = float(input("Digite o c : "))
        print(resolve_equacao(a,b,c))
    else:
        print("flw")
        break

4)
Numa sala hÃ¡ i = 5 linhas e j = 10 colunas, em cada linha por coluna hÃ¡ uma cadeira. Devido ao covid
deve haver distanciamento de uma cadeira entre cada pessoa, tanto na vertical quanto na horizontal.
FaÃ§a um programa que compute quantas pessoas podem se sentar e imprima a matriz com 0 nos lugares proibidos
e 1 nos lugares permitidos.
'''

def monta_sala(linhas, colunas):
    sala = []
    for i in range(linhas):
        sala.append([])
        for j in range(colunas):
            if i%2==0:
                if j%2==0:
                    sala[i].append(1)
                else:
                    sala[i].append(0)
            else:
                if j%2==0:
                    sala[i].append(0)
                else:
                    sala[i].append(1)
    return sala
sala = monta_sala(5,10)
qtd = 0
for i in range(5):
    qtd +=sum(sala[i])
    print(sala[i])
print(qtd)

#import matplotlib.pyplot as plt
#plt.imshow(sala)
#plt.show()

#1 0 1 0
#0 1 0 1
#1 0 1 0
#for p in range(10):
#    if p%2==0:
#        print(1,end=' ')
#    else:
#        print(0,end=' ')
#print('\n')
#for q in range(10):
#    if q%2==0:
#        print(0,end=' ')
#    else:
#        print(1,end=' ')




