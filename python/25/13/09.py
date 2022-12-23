############### DicionÃ¡rios ##############
#dicionario = {"key" : "value"}
#print(dicionario["key"])
#dicionario["new_key"] = [1,2,3,4]
#dicionario["key"] = "iusdhiudshf"
#print(dicionario)
#print(dicionario["new_key"])
#print(dicionario.keys())
#print(dicionario)
#print(dicionario.values())
#print(dicionario.items())

#nomes = {"alunos":["felipe","claudio","gustavo"],"professores":["Danilo","Edson","Ronqui"]}
nomes = {"alunos":[],"professores":[]}
#nomes["alunos"].append("Vinicius")
#print(nomes)
'''
while True:
    resposta = input("Voce quer cadastrar professores ou alunos ? : ")
    if resposta == "alunos":
        aluno = input("Diga o nome : ")
        nomes[resposta].append(aluno)
    elif resposta == "professores":
        professores = input("Diga o nome : ")
        nomes[resposta].append(professores)
    else:
        print("tchau")
        break
print(nomes)
'''
from random import randint

dic = {"oi":["olÃ¡","eai","salve salve"],"tchau":["flw","Ã©nois"],"bom dia":["oi","boa tarde"]}
#saudacao = input("diga oi ou tchau ou bom dia : ")
#print(dic[saudacao][randint(0,len(dic[saudacao])-1)])
#if saudacao == "oi":
#    print(dic["oi"])
#elif saudacao == "tchau":
#    print(dic["tchau"])
#elif saudacao == "bom dia":
#    print(dic["bom dia"])

#dic = {"chave" : ["valor",[[1,2],[3,4]]]}
#print(dic)
#dic["nova chave"] = "novo valor"
#print(dic)

#print(dic)
#for key in dic.keys():
#    dic[key].append(str(key))
#    print(dic[key])

#crie um dicionario com a chave "par" e coloque lÃ¡ os 10 primeiros numeros pares
#adicione uma chave "impar" e coloque lÃ¡ os 10 primeiros numeros impares
#1) crie um dicionario com a chave "float" e preencha a chave com 10 numeros float
#2) crie uma chave "int" e preencha com 10 numeros int
#3) exiba o conteudo de cada chave utilizando um for
#4) crie uma chave "soma" que recebe a soma dos valores na chave int e na chave float
#5) crie uma chave "quadrados" e nela coloque os 10 primeiros quadrados (i**2)
#6) crie uma chave "cubos" e coloque os 10 primeiros numeros ao cubo


numeros = {"par" : [], "impar" : []}
for i in range(10):
    if i%2==0:
        numeros["par"].append(i)
    else:
        numeros["impar"].append(i)

numeros = {"par" : []}
for i in range(10):
    if i%2==0:
        numeros["par"].append(i)
numeros["impar"] = []
for i in range(10):
    if i%2==1:
        numeros["impar"].append(i)
#print(numeros)

numeros = {"float" : [1.2,3.7,3.2,7.6,0.1,0.4,0.5,1.3,1.6,0.2]}
numeros["int"] = [0,1,2,3,4,5,6,7,8,9]
#for key in numeros.keys():
#    print(numeros[key])

numeros["soma"] = []
for i in range(10):
    soma = numeros["float"][i] + numeros["int"][i]
    numeros["soma"].append(soma)
#print(numeros)

numeros["quadrados"] = []
numeros["cubos"] = []
for i in range(10):
    numeros["quadrados"].append(i**2)
    numeros["cubos"].append(i**3)
#print(numeros)

#crie uma chave primos e coloque os 10 primeiros primos lÃ¡

num = 15
#7%2==1
#7%3==1
#7%4==3
#7%5==2
#7%6==1
def eh_primo(num):
    primo_ou_nao = False
    for i in range(2,num):
        if num%i==0:
            break
        elif i ==num-1:
            primo_ou_nao = True
    return primo_ou_nao

numeros["primos"] = [2]

for i in range(100):
    if eh_primo(i) == True:
        numeros["primos"].append(i)
print(numeros["primos"])
