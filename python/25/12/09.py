################## DicionÃ¡rios ################

dic = {"key" : ["value","valor"]}
#print(type(dic["key"]))
dic["chave"] = "nova chave"
#print(dic["chave"])
#print(dic)
#print(dic.keys())
dic["aluno"] = "danilo"
#print(dic.keys())
#for nome in dic.keys():
#    print(nome)
#print(dic.values())
#print(dic.items())
#del dic["key"]
#print(dic)

dic["aluno"] = "rafael"
for nome in dic.keys():
    if type(dic[nome]) is list:
        dic[nome].append("valores")
#    print(dic[nome])

#dic = {"alunos":[],"professores":[]}
#while True:
#    resposta = input("VocÃª deseja adicionar alunos ou professores (nao para sair) : ")
#    if resposta == "alunos":
#        dic[resposta].append(input("digite o nome do aluno : "))
#    elif resposta == "professores":
#        dic[resposta].append(input("digite o nome do professor : "))
#    else:
#        print("\n\n")
#        break
#alunos = dic["alunos"]
#professores = dic["professores"]
#print(f"esses sÃ£o os alunos : {alunos} e esses sÃ£o os professores : {professores}")
#print(dic)

def primo(numero):
    for i in range(2,numero):
        if numero%i==0:
            return False
        elif i == numero-1:
            return True
def par(numero):
    if numero %2==0:
        return True
    else:
        return False
dicionario_de_numeros = {"pares":[],"Ã­mpares":[]}
#print(dicionario_de_numeros)
for i in range(10):
    if par(i):
        dicionario_de_numeros["pares"].append(i)
    else:
        dicionario_de_numeros["Ã­mpares"].append(i)
#print(dicionario_de_numeros)
#print(f"os numeros Ã­mpares sao {dicionario_de_numeros['Ã­mpares']}")
#print(f"os numeros pares sao {dicionario_de_numeros['pares']}")

dicionario_de_numeros["primos"] = [2]
for i in range(10):
    if primo(i):
        dicionario_de_numeros["primos"].append(i)
#print(dicionario_de_numeros)

mercadinho = {"frutas" : ["abacaxi"],"peso" : [400], "preÃ§o" : [5]}
#print(mercadinho.keys())
mercadinho["frutas"].append("banana")
mercadinho["peso"].append(200)
mercadinho["preÃ§o"].append(2)
#print(mercadinho)

'''
while True:
    resposta = input("voce gostaria de cadastrar uma nova fruta ? ")
    if resposta=="sim":
        fruta = input("digite o nome da nova fruta : ")
        mercadinho["frutas"].append(fruta)
        peso = input("digite o peso da fruta : ")
        mercadinho["peso"].append(peso)
        preÃ§o = input("digite o preÃ§o da fruta : ")
        mercadinho["preÃ§o"].append(preÃ§o)
    else:
        print(f"essas sÃ£o as frutas : {mercadinho}")
        break




while True:
    resposta = input("voce gostaria de cadastrar uma nova fruta ? ")
    if resposta=="sim":
        fruta = input("digite o nome da nova fruta : ")
        peso = input("digite o peso da fruta : ")
        preÃ§o = input("digite o preÃ§o da fruta : ")
        lista = [fruta,peso,preÃ§o]
        i = 0
        for key in mercadinho.keys():
            mercadinho[key].append(lista[i])
            i+=1
    else:
        print(f"essas sÃ£o as frutas : {mercadinho}")
        break

print(mercadinho)


import pandas as pd
mercadinho = pd.DataFrame(mercadinho)
print(mercadinho)

'''

#emocoes = {"feliz" : ":)","triste" : ":("}
#print(emocoes['feliz'])
#frase = input("digite se vc ta feliz ou triste : ")
#if "feliz" in frase:
#    frase = frase.replace("feliz",emocoes["feliz"])
#elif "triste" in frase:
#    frase = frase.replace("triste",emocoes["triste"])
#print(frase)


#1) crie um dicionario com a chave "float" e preencha a chave com 10 numeros float
#2) crie uma chave "int" e preencha com 10 numeros int
#3) exiba o conteudo de cada chave utilizando um for
#4) crie uma chave "soma" que recebe a soma dos valores na chave int e na chave float
#5) crie uma chave "quadrados" e nela coloque os 10 primeiros quadrados (i**2)
#6) crie uma chave "cubos" e coloque os 10 primeiros numeros ao cubo

dicionario = {"float" : [1.7,3.0,0.4,0.3,1.2,5.4,7.8,3.9,9.1,2.0]}
#print(len(dicionario["float"]))
dicionario["int"] = [1,2,3,4,5,6,7,8,9,10]
#print(len(dicionario["int"]))
#for key in dicionario:
    #print(f"na chave {key} tem os seguintes elementos:")
    #print(dicionario[key])

dicionario["soma"] = []
for i in range(10):
    soma = dicionario["int"][i] + dicionario["float"][i]
    dicionario["soma"].append(soma)
#print(dicionario["soma"])

dicionario["quadrados"] = []
dicionario["cubos"] = []
for i in range(10):
    dicionario["quadrados"].append(i**2)
    dicionario["cubos"].append(i**3)
#print("esses sao os 10 primeiros quadrados : ",dicionario["quadrados"])
#print("esses sao os 10 primeiros cubos : ",dicionario["cubos"])


#verifique se hÃ¡ chaves em comum aos dicionarios e caso haja, crie um novo dicionario com
#o merge do conteudo das chave
dic_1 = {"int" : [1,2,3,4,5,6],"float" : [1.7,3.0,0.4,0.3,1.2]}
dic_2 = {"int" : [6,5,7,8,2,1],"nomes":["danilo","rafael"]}
#dic_3 = {"int" : [1,2,3,4,5,6,6,5,7,8,2,1]}
dic_3 = {}
for key1 in dic_1.keys():
    if key1 in dic_2.keys():
        extendida = dic_1[key1]+dic_2[key1]
        dic_3[key1] = extendida
print(dic_3)
