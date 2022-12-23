l1 = [1, 0, 1]
l2 = [1, 1, 0, 1, 0, 1, 0, 0, 1, 1, 0, 1, 0, 1]
count = 0
for i in range(len(l2)-len(l1)):
    for j in range(len(l1)):
        if l2[i+j] == l1[j]:
            if j == len(l1)-1:
                count+=1
        else:
            break
print(count)

############### exercicio 2 #####################

lista1= [1, 2, 2, 3, 4, 5, 7, 6, 4]
lista2= [2, 5, 7, 1, 9, 18]
lista3 = lista1+lista2
lista_uniao = []
for elemento in lista3:
    if elemento not in lista_uniao:
        lista_uniao.append(elemento)
print(lista_uniao)