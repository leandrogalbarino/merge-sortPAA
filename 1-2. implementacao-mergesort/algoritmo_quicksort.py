import numpy as np

# Função para particionar o array
def partition(array, left, right):
    # Usamos a mediana de três como pivô
    mid = left + (right - left) // 2
    pivot_candidates = [(array[left], left), (array[mid], mid), (array[right], right)]
    pivot, pivot_index = sorted(pivot_candidates)[1]  # Mediana de três

    # Coloca o pivô no final
    array[pivot_index], array[right] = array[right], array[pivot_index]

    i = left - 1
    for j in range(left, right):
        if array[j] <= pivot:
            i += 1
            array[i], array[j] = array[j], array[i]

    array[i + 1], array[right] = array[right], array[i + 1]
    return i + 1

# Função principal do QuickSort
def sort(array, left, right):
    stack = [(left, right)]  # Usar uma pilha para evitar recursão

    while stack:
        left, right = stack.pop()
        if left < right:
            pi = partition(array, left, right)  # Particiona o array
            # Coloca as subpartições na pilha
            stack.append((left, pi - 1))  # Ordena a parte esquerda
            stack.append((pi + 1, right))  # Ordena a parte direita
