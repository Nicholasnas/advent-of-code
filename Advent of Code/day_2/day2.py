import numpy as np

def ler_dados():

    relatorios = []
    with open(r'Advent of Code\\day_2\\arq.txt', 'r') as file:
        for line in file:
            relatorio = list(map(int, line.split()))
            relatorios.append(relatorio)

    return relatorios

def is_safe(relatorio):
    cres = relatorio[0] < relatorio[1]
    if cres:
        for i in range(len(relatorio) - 1):
            diff = relatorio[i+1] - relatorio[i]
            if not (1 <= diff <= 3):
                return False
        
        return True
    else:
        for i in range(len(relatorio) -1):
            diff = relatorio[i+1] - relatorio[i]
            if not (-3 <= diff <= -1):
                return False
        
        return True
    
def part_dois(relatorio):
    for i in range(len(relatorio)):
        if is_safe(relatorio[:i] + relatorio[i+1:]):
            return True
    
    return False

## precisa verificar se o relatorio esta crescendo ou descrescendo
def crescendo(relatorio):
    
    verifica = [False] * (len(relatorio)- 1)
    for i in range(len(relatorio)-1):
        if relatorio[i] < relatorio[i+1] and abs(relatorio[i+1] - relatorio[i]) <= 3:
            verifica[i] = True
        
    return all(verifica)

def decrescendo(relatorio):
    verifica = [False] * (len(relatorio)- 1)
    for i in range(len(relatorio)-1):
        if relatorio[i] > relatorio[i+1] and abs(relatorio[i+1] - relatorio[i]) <= 3:
            verifica[i] = True
    return all(verifica)

def verificar_relatorio(relatorios):
    cont = 0
    for relatorio in relatorios:
        if crescendo(relatorio) or decrescendo(relatorio):
            cont += 1
    
    print(cont)

def main():
    relatorios = ler_dados()
    cont = 0
    for relatorio in relatorios:
        if part_dois(relatorio):
            cont += 1
    
    print(cont)


main()