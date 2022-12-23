####################


dic = {}

for i in range(5):
    for j in range(10):
        if i+2<=4 and j+2<=9:
            dic[(i,j)] = [(i+2,j+2)]
            if i+3 <=4 and j+3<=9:
                dic[(i,j)].append((i+3,j+3))
        else:
            dic[(i,j)]=None
print(dic)