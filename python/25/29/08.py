########## exercÃ­cios ##########


#gere a lista dos n primeiros pares (3 primeiros pares deve retornar [2,4,6])
def gera_par(n_primeiros):
    lista_pares = []
    i=0
    while len(lista_pares)<n_primeiros:
       if i%2==0:
           lista_pares.append(i)
       i+=1
    return lista_pares

#n_primeiros_pares = gera_par(10)
#print(n_primeiros_pares)

#gere a lista dos n primeiros primos (5 primeiros primos deve retornar [2,3,5,7,11])

#7 Ã© primo?
#7%2==1
#7%3==1
#7%4==3
#7%5==2
#7%6==1

def checa_primo(numero):
    var = False
    for i in range(1,numero):
       if numero%i==0 and i!=1:
           var = False
           break
           #return False
       elif i==numero-1:
           var = True
           #return True
    return var

def gera_primo(n_primeiros):
    lista_primos = []
    i=1
    while len(lista_primos)<n_primeiros:
        if checa_primo(i):
            lista_primos.append(i)
        i+=1
    return lista_primos

#n_primeiros_primos = gera_primo(100)
#print(n_primeiros_primos)

#escreva uma funÃ§Ã£o que recebe uma lista contendo listas e retorna uma lista "planificada"
#Original: [0, 10, [20, 30], 40, 50, [60, 70, 80], [90, 100, 110, 120]]
#Planficada:[0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120]
#realiza o teste pelo tamanho

#i = 0
#print(type(i) is int)

def planifica_lista(orig):
    planificada = []
    for elem in orig:
        if type(elem) is list:
            #print(elem)
            for elem_lista in elem:
                planificada.append(elem_lista)
        else:
            planificada.append(elem)
    return planificada
#print(original)
#print(planificada)
original =  [0, 10, [20, 30], 40, 50, [60, 70, 80], [90, 100, 110, 120]]
#print(original)
plana = planifica_lista(original)
#print(plana)

nova_lista = [1,2,[4,5,78],[21,34],23,35]
#print('\n')
#print(nova_lista)
plana = planifica_lista(nova_lista)
#print(plana)

#escreva uma funÃ§Ã£o que recebe uma lista de inteiros e printa o de maior ocorrencia e o numero de ocorrencias

#item com mais ocorrencias : 2, nÂº ocorrencias = 4

#[1,2,2,2,3,3,4,5,6,6,6]
numeros = [2, 3, 8, 4, 7, 9, 8, 2, 6, 5, 1, 6, 1, 2, 3, 4, 6, 9, 1, 2]
#print(numeros)
numeros.sort()
print(numeros)
numero_ocorrencia = []
i=0
j=0
while i <len(numeros)-1:
    n_ocorrencia = 1
    while numeros[i]==numeros[i+1] and i<len(numeros)-2:
        n_ocorrencia +=1
        #print(n_ocorrencia)
        i+=1

    numero_ocorrencia.append(n_ocorrencia)
    #print(numero_ocorrencia)
    i += 1


print('numero_ocorrencia : ',numero_ocorrencia)

#numa lista heterogenea ([1, 'abcd', 3, 1.2, 4, 'xyz', 5, 'pqr', 7, -5, -12.22])
#conte o numero de inteiros contidos ali, resposta Ã© 4


def conta_inteiros(heterogenea):
    count=0
    for elem in heterogenea:
        if type(elem) is int:
            count+=1
    return count
heterogenea = [1, 'abcd', 3, 1.2, 4, 'xyz', 5, 'pqr', 7, -5, -12.22]
num_inteiros = conta_inteiros(heterogenea)
#print("o numero de inteiros contido nessa lista Ã©",num_inteiros)

#dada uma lista heterogenea (['Python', 3, 2, 4, 5, 'version']) encontre o maior e o menor nÃºmero dentro dela
lista = ['Python', 3, 2, 4, 5, 'version']

def remove_string(lista):
    nova_lista = []
    for elem in lista:
        if type(elem) is int:
            nova_lista.append(elem)
    return nova_lista

def busca_menor_maior(lista):
    nova_lista = remove_string(lista)
    menor = nova_lista[0]
    maior = nova_lista[0]
    for elem in nova_lista:
        if elem < menor:
            menor = elem
        if elem > maior:
            maior = elem
    return[menor,maior]
#print(busca_menor_maior(lista))
#print(menor, maior)



