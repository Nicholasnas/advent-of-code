
from collections import Counter

def mostrar_lista(lista):
    for valor in lista:
        print(valor)

def distancia_entre_os_lugares(lista1:list, lista2:list):
    
    # diference - first part
    lista_distancia = []
    resultado = 0
    for i in range(len(lista1)):
        valor = abs(lista1[i] - lista2[i])
        resultado += valor
        lista_distancia.append(valor)

    # for classic version
    cont = [0] * 1000
    soma2 = 0
    for i in range(len(lista1)):
        for j in range(len(lista2)):
            if lista1[i] == lista2[j]:
                cont[i] += 1
        
        soma2 += lista1[i] * cont[i]

    # New version with list compreshion and zip
    cont2 = [lista2.count(x) for x in lista1]
    soma3 = sum([x*y for x,y in zip(lista1, cont2)])

    # output program
    print('primeira parte: ',resultado)
    print('Segunda parte v2:',soma2) # 54648217
    print("New version python:", soma3) # 

def main():
    path = 'Advent of Code\\day_1\\file.txt'
    lista1 = []
    lista2 = []

    with open(path, 'r') as arq:
        for linha in arq:
            num1, num2 = linha.split()
            lista1.append(int(num1))
            lista2.append(int(num2))

    lista1.sort()
    lista2.sort()
    distancia_entre_os_lugares(lista1, lista2)

    # print(distancia_entre_os_lugares(lista1, lista2))
main()