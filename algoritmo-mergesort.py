import pandas as pd 
import numpy as np

def merge(array, left, middle, right):
    n1 = middle - left + 1
    n2 = right - middle
    left_array = np.zeros(n1)
    right_array = np.zeros(n2)

    for i in range(n1):
        left_array[i] = array[left + 1]
    for j in range(n2):
        right_array[j] = array[middle + 1 + j]
    i = 0
    j = 0
    k = left
    while (i < n1) and (j < n2):
        if left_array[i] <= right_array[j]:
            array[k] = left_array[i]
        else:
            array[k] = right_array[j]
        k+= 1
    while i < n1:
        array[k] = left_array[i]
        i+= 1
        k+= 1
    while j < n2:
        array[k] = right_array[j]
        j+=1
        k+=1


def merge_sort(array, left, right):
    if left < right:
        middle = left + (right - left) / 2
        merge_sort(array, left, middle)
        merge_sort(array, middle + 1, right)

        merge(array, left, middle, right)




# Gera uma matriz de 3 números aleatórios uniformemente distribuídos no intervalo [0, 10).
# Retorna um array de float64 por padrão.
random_array = np.random.rand(3) * 10

# Converte o array para o tipo de dados int32.
int_array = random_array.astype(np.int32)

# Imprime as matrizes geradas
print(random_array)
print(int_array)