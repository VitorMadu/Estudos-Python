############# dicionario ############
'''dicionario = {"nome" : "Danilo"}
print(dicionario["nome"])
dicionario["idade"] = 25
print(dicionario)
dicionario["nome"] = "caio"
print(dicionario)
dicionario["nome"] = []
print(dicionario["nome"])
dicionario["nome"].append("Danilo")
print(dicionario["nome"])
dicionario["nome"].append("caio")
print(dicionario)
print(dicionario["nome"][1])
for key in dicionario.keys():
    print(key)
numeros = {"um": "1", "dois": "2", "tres": "3", "quatro": "4", "cinco": "5", "seis": "6",
           "sete": "7", "oito": "8", "nove": "9", "zero": "0"}
print(numeros.keys())
frase = "um dois"
print(frase)
for key in numeros.keys():
    if key in frase:
        frase = frase.replace(key,numeros[key])
print(frase)
'''

#lista = [5,4,3,7,6,1,2]
def acha_maior_menor(lista):
    indice_menor = 0
    indice_maior = 0
    menor = lista[indice_menor]
    maior = lista[indice_maior]
    for i in range(len(lista)):
        print(f"{lista[i]} < {menor}")
        if lista[i] > maior:
            maior = lista[i]
            indice_maior = i
        if lista[i] < menor:
            menor = lista[i]
            indice_menor = i
            print(menor)
    return indice_maior, indice_menor, maior, menor
carro = {'modelo': ['Ferrari', 'Porsche', 'Aston Martin', 'Rolls Royce', 'Lamborghini'],
         'ano': ['2022', '2021', '2014', '2010', '2018'],
         'preco': [1, 1.5, 0.9, 0.8, 1.2]}
ind_max, ind_min, max, min = acha_maior_menor(carro["preco"])
print(f"o carro mais barato Ã© o {carro['modelo'][ind_min]} e vale {min} e foi fabricado no ano {carro['ano'][ind_min]}")

#print(f"o maior elemento Ã© {maior} e estÃ¡ na posiÃ§Ã£o {indice_maior}")
#print(f"o menor elemento Ã© {menor} e estÃ¡ na posiÃ§Ã£o {indice_menor}")

