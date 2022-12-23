############ tratamento de exceÃ§Ãµes ##############
#entra no else quando o try funciona
#o finally SEMPRE Ã© executado

'''
i=0
while i<3:
    a = input("digite um numero : ")
    try:
        a = int(a)
        if a%2==0:
            print("Ã© par")
        else:
            print("Ã© Ã­mpar")
        break
    except:
        print("voce deve digitar um numero")
    else:
        print("parabens vc digitou um numero")
    finally:
        i+=1
        if type(a) is int:
            print("fim da execuÃ§Ã£o")
        if i!=3:
            print(f"voce sÃ³ tem mais {3-i} tentativas")
        else:
            print("acabaram suas tentativas")

try:
    c=0
    print(c)
    b = 120
    b = len(b)
    a = 'abc'
    a = int(a)
except TypeError:
    print("deu erro de tipo")
except ValueError:
    print("a varaiavel nao Ã© numerica")
except Exception as e:
    print(f"Deu erro : {e}")


try:
    a = 'abc'
    a = int(a)
    b = len(120)
except TypeError:
    print("erro de tipo")
except Exception as e:
    print(e)

lista = [23,56,72]
try:
    indice = int(input("digite a casa da lista que voce quer exibir : "))
    print(lista[indice])
except ValueError:
    print("voce deve digitar uma variavel numerica")
except IndexError:
    print(f"voce sÃ³ pode exibir atÃ© o Ã­ndice {len(lista)-1}")
except Exception as e:
    print(f"deu erro : {e}")
    raise


#string = "oi eu sou o danilo"
#print(string.split(" "))
try:
    inteira = 2
    inteira = inteira.split(",")
    raiz = sqrt(2)
    a = 'abc'
    a = int(a)
    b = 120
    b = len(b)
    print(c)
except NameError:
    print("funÃ§Ã£o invalida")
except AttributeError:
    print("erro de atributo")
except Exception as e:
    print("deu erro")
    raise

#tente printar uma variavel que nao existe e quando der erro avise isso ao usuario
#tente pegar o comprimento de um numero e avise ao usuario que nao Ã© possÃ­vel
#tente acessar uma casa da lista que nao existe, e pergunte ao usuario se ele gostaria de aumentar
#o tamanho da lista

#try:
#    print(variavel)
#except:
#    print("voce tentou exibir uma variavel que nao existe")

#numero = 130
#try:
#    print(len(numero))
#except TypeError:
#    print("numeros inteiros nao tem o mÃ©todo len")

lista_de_alunos = ["vinicius","rafael","roberto"]
i=0
print("Mostrando os alunos do curso")
while True:
    try:
        print(f"A pessoa {lista_de_alunos[i]} Ã© aluno/a")
        i+=1
    except:
        print("nÃ£o hÃ¡ mais alunos")
        s_ou_n = input("voce quer adicionar alunos na lista ?")
        if s_ou_n == "sim":
            lista_de_alunos.append(input("digite o nome do novo aluno : "))
        else:
            print("que chato, aqui estÃ£o todos os alunos:")
            print(lista_de_alunos)
            break
'''
import time
nome = "Danilo"
for i in nome:
    print(i,end='')
    time.sleep(0.5)


#for i in range(10):
#    print(i,end=' ')