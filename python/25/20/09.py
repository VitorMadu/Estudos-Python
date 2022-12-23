##################### checkpoint #####################
# fibo[0]=1, fibo[1] =1
# fibo[2] = fibo[0] + fibo[1]
# fibo[3] = fibo[1] + fibo[2]
# ...
# fibo[i+2] = fibo[i] + fibo[i+1]

def gera_fibo(num):
    fibo = [1,1]
    for i in range(num-2):
        soma = fibo[i] + fibo[i+1]
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

def gera_fibonacci(num):
    fibo = [1,1]
    num1 = 1
    num2 = 1
    while len(fibo)<num:
        num3 = num1 + num2
        fibo.append(num3)
        num1 = num2
        num2 = num3
    return fibo
numero = 50
#fibonacci_2 = gera_fibonacci(numero)
fibonacci = gera_fibo(numero)
#fibona = gen_fibo(numero)
#print(fibonacci)
#print(fibona)
#print(fibonacci_2)

def conta_par(lista):
    pares = 0
    for num in lista:
        if num%2==0:
            pares+=1
    return pares

#par = conta_par(fibonacci)
#print(par)
#7%1==0
#7%2==1 # 7 = 3*2 + 1
#7%3==1 # 7 = 2*3 + 1
#7%4==3 # 7 = 1*4 + 3
#7%5==2 # 7 = 1*5 + 2
#7%6==1 # 7 = 1*6 + 1
#7%7==0



#10%6==4
#10%7==3
#10%8==2
#10%9==1

#35%18==17
#35%19==16
#35%20==15


#9%2==1
#9%3==0
def conta_primo(lista):
    if 2 in lista:
        primos = 1
    else:
        primos =0
    j=0
    for num in lista:
        j+=1
        print(j)
        for i in range(2,num):
            #print(f"{num}%{i}=={num%i}")
            if num%i==0:
                break
            elif i==num-1:
                primos+=1
    return primos
#numero_primos = conta_primo(fibonacci)
#print(numero_primos)

########################## challenge ##########################

condicao = False
#while():
#    if condicao == True:
#        def par(num):
#            if num%2==0:
#               print(f"{num} Ã© par")
#            else:
#               print("nao Ã© par")
#            return
#def realiza_cadastro(nome,endereco,data):
#    cadastro = [nome,endereco,data]
#    print("cadastro realizado com sucesso!!!")
#    return cadastro

#cad = realiza_cadastro("danilo","jundiai","19/02/1997")
#print(cad)

############################## dicionÃ¡rios ################################

dicionario = {"nome" : ["danilo"]}
print(dicionario["nome"])
dicionario["data"] = ["19/02/1997"]
print(dicionario)
print(dicionario.keys())
for key in dicionario.keys():
    print(key)
#del dicionario["nome"]
dicionario["nome"].append("vinicius")
dicionario["data"].append("20/01/2000")
dicionario["endereÃ§o"] = ["jundiai","sao paulo"]
print(dicionario,'\n\n\n')

"pip install pandas"
import pandas as pd
pessoas = pd.DataFrame(dicionario)
#print(pessoas)
#criem um dicionario com a chave par e coloque la uma lista com os 10 primeiros numeros pares
#criem a chave impar e coloque la uma lista com os 10 primeiros numeros impares

dicionario = {"par" : []}
i=0
print(dicionario)
while len(dicionario["par"])<10:
    if i%2==0:
        dicionario["par"].append(i)
    i+=1
print(dicionario)
dicionario["impar"] = []
i=0
while len(dicionario["impar"])<10:
    if i%2==1:
        dicionario["impar"].append(i)
    i+=1
print(dicionario)

dicionario = pd.DataFrame(dicionario)
print(dicionario)