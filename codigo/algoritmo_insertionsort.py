# Importa a biblioteca numpy como np, que será utilizada para gerar o array de números aleatórios.
import numpy as np

# Função para aplicar o algoritmo de Insertion Sort em um array.
def sort(array):
    # O laço começa do segundo elemento até o final do array.
    for i in range(1, array.size):
        chave = array[i]  # Define o valor atual a ser inserido na posição correta.
        j = i - 1  # Começa a comparar o elemento anterior.

        # Enquanto o elemento anterior for maior que o valor atual (chave), mova-o uma posição para a direita.
        while j >= 0 and array[j] > chave:
            array[j + 1] = array[j]  # Move o elemento maior uma posição à frente.
            j -= 1  # Decrementa j para continuar verificando os elementos anteriores.

        # Insere a chave na posição correta após mover todos os elementos maiores.
        array[j + 1] = chave