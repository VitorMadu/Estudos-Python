######## checkpoint #########


#fibo[0]=1, fibo[1]=1
#1+1 = 2 #fibo[2] = fibo[0] + fibo[1]
#2+1 = 3 #fibo[3] = fibo[1] + fibo[2]
#3+2 = 5 #fibo[4] = fibo[2] +fibo[3]
#fibo[i+2] = fibo[i] + fibo[i+1]
def gera_fibonacci(num):
    fibo = [1, 1]
    for i in range(num-2):
        soma = fibo[i]+fibo[i+1]
        fibo.append(soma)
    return fibo

def gen_fibo(num):
    fibo = [1,1]
    i=0
    while len(fibo)<num:
        soma = fibo[i]+fibo[i+1]
        fibo.append(soma)
        i+=1
    return fibo
#print("FIBO : ",gen_fibo(40))
numeros = gera_fibonacci(20)
#print(numeros)

def conta_par(lista):
    count = 0
    for num in lista:
        if num%2==0:
            count+=1
    return count

#print(conta_par(numeros))


#7
#7%2==1 (7 = 3*2 + 1)
#7%3==1 (7 = 2*3 + 1)
#7%4==3 (7 = 4*1 + 3)
#7%5==2 (7 = 5*1 + 2)
#7%6==1 (7 = 6*1 + 1)

#15%2==1 (15 = 7*2 + 1)
#15%3==0 (15 = 5*3 + 0)

def verifica_primo(lista):
    if 2 in lista:
        count=1
    else:
        count=0
    for num in lista:
        for i in range(2,num):
            #print(f"{num}%{i} = {num % i}")
            if num%i==0:
                break
            elif i==num-1:
                count+=1

    return count

numeros = gera_fibonacci(15)
#print(numeros)
#print(verifica_primo(numeros))

####################### challenge ########################
condicao = True
#while condicao2:
#    if condicao1:
#        def par(num):
#            if num%2==0:
#                print(f"{num} Ã© par")
#            return
#par(6)

#def realiza_cadastro():
#    resposta = input("voce quer realizar um cadastro ? ")
#    if resposta == "sim":
#        cadastro = ["nome", "data", "endereÃ§o"]
#    print("cadastro realizado com sucesso")
#    return cadastro

#cadastro = realiza_cadastro()
#print(cadastro)


#################### dicionÃ¡rios #####################

dicionario = {"nome":"Danilo"}
#print(dicionario)
dicionario["nascimento"] = "19/02/1997"
#print(dicionario["nascimento"])
dicionario["nome"] = "vinicius"
#print(dicionario)

#print(dicionario.keys())
#print(dicionario.values())
#del dicionario["nome"]

#for key in dicionario.keys():
#    print(dicionario[key])

numeros = {"pares" : []}
for i in range(10):
    if i%2==0:
        numeros["pares"].append(i)
numeros["impar"] = []
for i in range(10):
    if i%2==1:
        numeros["impar"].append(i)
#print(numeros)



#faÃ§a um dicionario com as chaves par, impar e fibonacci com listas vazias
#preencha o dicionaria com 100 numeros pares, impares e de fibonacci

dicionario ={"par":[],"impar":[]}
dicionario["par"] = list(range(0,100,2))
dicionario["impar"] = list(range(1,99,2))
#print(dicionario)

fibo = [1,1]
for i in range(98):
    soma = fibo[i]+fibo[i+1]
    fibo.append(soma)
dicionario["fibonacci"] = fibo
#print(dicionario)

dic1 = {"int" : [1,2,3,4,5,6,7], "float": [0.3,5.1,2.7]}
dic2 = {"string":["danilo","vinicius"],"float":[1.2,4.6,2.1],"int":[2,3,43,76,21]}
#dic3 = {"int" : [1,2,3,4,5,6,7,2,3,43,76,21],"float":[1.2,4.6,2.1,0.3,5.1,2.7]}
#com esses dois dicionarios, verifique se hÃ¡ chaves em comum e faÃ§a um merge do conteudo das chaves
dic2={"nome":["danilo","vinicius","bruno"],"data":["19/02/1997","29/06/1990"]}
dic3 = {}
#dic3["nova"] = []
#print(dic3)
for key1 in dic1.keys():
    for key2 in dic2.keys():
        if key1 == key2:
            print(f"{key1} Ã© uma chave em comum aos dois dics")
            dic3[key1] = dic2[key2] + dic1[key1]
            print(dic3)
print(dic3)




