#dicionÃ¡rios
dicionario = {'chave' : 'valor','nova_chave' : 'novo_valor'}
#print(dicionario['chave'])
dicionario['nome'] = ['Danilo']
#print(dicionario)
dicionario['nome'].append("Rafael")
#print(dicionario)
dicionario[2] = 'dois'
#print(dicionario)
#print(dicionario.keys())
#print(dicionario.values())
#print(dicionario.items())

#resposta = input("Diga olÃ¡ : ")
#if resposta == "olÃ¡":
#    print("oi")

#dicionario = {"olÃ¡":"oi","tchau":"flw"}
#resposta = input("Diga olÃ¡ : ")
#print(dicionario[resposta])

#import random
#print(random.choice(dicionario["olÃ¡"])) CHOICE Ã‰ ESCOLHA EM INGLES, RANDOM Ã‰ ALEATORIO

#dicionario = {"olÃ¡" : ["oi","eai","suave?"],"tchau" : ["flw","Ã©nois","atÃ©"]}
#resposta = input("Diga olÃ¡ : ")
#print(random.choice(dicionario[resposta]))

mercadinho = {"Frutas" : ["maÃ§Ã£","banana"], "PreÃ§o" : [2.00,3.00], "Validade" : ["16/08","25/08"]}
#print(mercadinho)
nova_fruta = ["abacaxi",4.00,"30/08"]
#chaves_mercadinho = ["Frutas","PreÃ§o","Validade"] (mercadinho.keys())
#zip(nova_fruta,chaves_mercadinho) = [("Frutas","abacaxi"),("PreÃ§o",4.00),("Validade","30/08")]
#i=0
#for key in mercadinho.keys():
#    mercadinho[key].append(nova_fruta[i])
#    i+=1
#print(mercadinho)

#print(list(zip(mercadinho.keys(),nova_fruta)))
for key,value in zip(mercadinho.keys(),nova_fruta):
    mercadinho[key].append(value)

#print(mercadinho)


import pandas as pd
mercadinho = pd.DataFrame(mercadinho)
#print(mercadinho)

#monte um dicionario com as chaves "par" e "Ã­mpar" e armazene nessas chaves os 100 primeiros numeros pares
#e os 100 primeiro numero impares

numeros = {"par" : [],"Ã­mpar" : []}

for i in range(200):
    if i%2==0:
        numeros["par"].append(i)
    else:
        numeros["Ã­mpar"].append(i)
#print(numeros)
del numeros["par"]
#print(numeros)
numeros["par"] = list(range(0,200,2))
#print(numeros)
numeros = pd.DataFrame(numeros)
#print(numeros)

matriz = {"3x3":[[1,2,3],[4,5,6],[7,8,9]],"4x4":[[1,2,3,4],[5,6,7,8],[9,10,11,12]]}
#print(matriz["3x3"])

#crie um dicionÃ¡rio com as chaves "quadrado" e "cubo" e preencha essas chaves com os umeros de 0 a 100 elevados
#ao quadrado e ao cubo

numeros = {"quadrados":[],"cubos":[]}
for i in range(100):
    numeros["quadrados"].append(i**2)
    numeros["cubos"].append(i**3)
#print(numeros)
#numeros = pd.DataFrame(numeros)
#print(numeros)

frase = "existem matrizes quadradas e existem matrizes retangulares"
dicionario = {"existem" : 2,"matrizes" : 2, "quadradas" : 1, "e" : 1, "retangulares" : 1}

palavras = frase.split(" ")
print(palavras)
print(list(set(palavras)))

palavras = {}
for palavra in set(frase.split(" ")):
    palavras[palavra] = 0
print(palavras)

for palavra in set(frase.split(" ")):
    for elemento in frase.split(" "):
        if elemento == palavra:
            palavras[palavra]+=1
print(palavras)