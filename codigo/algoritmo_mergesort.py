import pandas as pd 
import numpy as np

# Junta as partes do array, fazendo o merge 
# Esta função recebe um array e dois subarrays que foram divididos pela função merge_sort.
# Ela vai mesclar esses subarrays de volta em uma única parte ordenada no array original.
def merge(array, left, middle, right):
    # Define o tamanho dos dois subarrays a serem mesclados.
    n1 = middle - left + 1  # Tamanho do subarray esquerdo
    n2 = right - middle      # Tamanho do subarray direito

    # Cria dois arrays temporários para armazenar os valores do subarray esquerdo e direito.
    left_array = np.zeros(n1)
    right_array = np.zeros(n2)

    # Copia os dados relevantes do array principal para os arrays temporários.
    for i in range(n1):
        left_array[i] = array[left + i]
    for j in range(n2):
        right_array[j] = array[middle + 1 + j]

    # Inicializa os índices para percorrer o subarray esquerdo (i), direito (j) e o array original (k).
    i = 0
    j = 0
    k = left  # Índice inicial no array original

    # Mescla os dois subarrays enquanto houver elementos em ambos
    while (i < n1) and (j < n2):
        if left_array[i] <= right_array[j]:
            # Se o elemento do subarray esquerdo for menor ou igual, coloca no array original.
            array[k] = left_array[i]
            i += 1
        else:
            # Caso contrário, coloca o elemento do subarray direito.
            array[k] = right_array[j]
            j += 1
        k += 1

    # Copia os elementos restantes do subarray esquerdo (se ainda houver algum).
    while i < n1:
        array[k] = left_array[i]
        i += 1
        k += 1

    # Copia os elementos restantes do subarray direito (se ainda houver algum).
    while j < n2:
        array[k] = right_array[j]
        j += 1
        k += 1


# Função principal do Merge Sort.
# Enquanto o array tiver mais de um elemento, ele divide o array em duas partes, 
# chamando merge_sort recursivamente em cada metade.
def sort(array, left, right):
    if left < right:  # Condição de parada: se left >= right, o array já está ordenado.
        # Calcula o índice do meio para dividir o array.
        middle = left + (right - left) // 2

        # Chama merge_sort recursivamente para a metade esquerda.
        sort(array, left, middle)

        # Chama merge_sort recursivamente para a metade direita.
        sort(array, middle + 1, right)

        # Após dividir as duas partes, chama a função merge para ordená-las e combiná-las.
        merge(array, left, middle, right)

