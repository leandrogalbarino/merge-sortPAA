# Importa a biblioteca numpy como np, que será utilizada para gerar o array de números aleatórios.
import numpy as np

# Função para aplicar o algoritmo de Insertion Sort em um array.
def sort(array):
    # O laço começa do segundo elemento até o final do array.
    for i in range(1, array.size):
        chave = array[i]  # Define o valor atual a ser inserido na posição correta.
        j = i - 1

        # Enquanto o elemento anterior for maior que o valor atual (chave), mova-o uma posição para a direita.
        while j >= 0 and array[j] > chave:
            array[j + 1] = array[j]  
            j -= 1 

        # Insere a chave na posição correta após mover todos os elementos maiores.
        array[j + 1] = chave