'''
matriz = [[1,2,3,4], [5,6,7,8], [9,10,11,12],[13,14,15,16]]
linhas = len(matriz)
colunas = len(matriz[0])
print(len((matriz)))
for i in range(linhas):
    for j in range(colunas):
        if matriz[i][j] %2 ==1:
            print(i,j, "elemento :",matriz[i][j])

#ache a posiÃ§Ã£o i j de todos os elementos Ã­mpares
#gere uma matriz 10x10 com 0 nas colunas pares

matriz = []
matriz.append([])
matriz.append([])
matriz.append([])
print(matriz)
matriz[0].append(1)
matriz[0].append(2)
matriz[0].append(3)
print(matriz)
'''
matriz = []
for i in range(10):
    matriz.append([])
    print(matriz[i])
    for j in range(10):
        if i%2==0:
            if j % 2 == 0:
                matriz[i].append(0)
            # print(matriz[i])
            else:
                matriz[i].append(1)
        else:
            if j % 2 == 0:
                matriz[i].append(1)
            # print(matriz[i])
            else:
                matriz[i].append(0)

#print("################\n\n\n\n")
#for i in range(10):
#    print(matriz[i])
#import matplotlib.pyplot as plt
#plt.imshow(matriz)
#plt.show()

#crie uma matriz 50x50 em que os elementos sejam i*j e conte quantos sÃ£o pares
num_pares=0
matriz = []
for i in range(1000):
    matriz.append([])
    for j in range(1000):
        matriz[i].append(i*j)
        if i*j%2==0:
            num_pares+=1
print(num_pares)
#print(matriz)
import matplotlib.pyplot as plt
plt.imshow(matriz)
plt.colorbar()
plt.hot()
plt.show()