import numpy as np

def ler_dados():
    relatorios = []
    with open(r'Advent of Code\\day_2\\arq.txt', 'r') as file:
        for line in file:
            relatorio = list(map(int, line.split()))
            relatorios.append(relatorio)

    return np.array(relatorios, dtype=object)

def first_solution(relatorio):
    diff  = np.diff(relatorio)
    # intervalo de crescimento 1 <= diff <= 3
    crescente = np.all((diff >= 1)& (diff <= 3))

    # intervalo decrescimento -3 <= diff <= -1
    decrescente = np.all((diff >= -3) & (diff <= -1))
    return crescente or decrescente

def secound_solution(relatorio):
    diff = np.diff(relatorio)
    # intervalo de crescimento 1 <= diff <= 3
    crescente = np.all((diff >= 1) & (diff <= 3))

    # intervalo decrescimento -3 <= diff <= -1
    decrescente = np.all((diff >= -3) & (diff <= -1))
    if crescente or decrescente:
        return True
    
    for i in range(len(relatorio)):
        new_relatorio = np.delete(relatorio, i)
        new_diff = np.diff(new_relatorio)

        # intervalo de crescimento 1 <= diff <= 3
        crescente = np.all((new_diff >= 1) & (new_diff <= 3))
        # intervalo decrescimento -3 <= diff <= -1
        decrescente = np.all((new_diff >= -3) & (new_diff <= -1))

        if crescente or decrescente:
            return True
    
    return False

def is_safe(relatorios):
    seguros = 0
    for relatorio in relatorios:
        if secound_solution(relatorio):
            print('seguro: ',relatorio)
            seguros +=1

    print(seguros)

def main():
    relatorios = ler_dados()
    is_safe(relatorios)

main()