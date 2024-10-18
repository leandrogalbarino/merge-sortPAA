import algoritmo_mergesort as merge
import algoritmo_insertionsort as insertion
import algoritmo_quicksort as quick
import numpy as np
import time


def gerar_arrays(tamanho=10000, max_valor=333001):
    # Gera uma matriz de números aleatórios uniformemente distribuídos no intervalo [0, max_valor).
    random_array = np.random.rand(tamanho) * max_valor
    int_array = random_array.astype(np.int32)

    # 1. Array totalmente ordenado (crescente)
    array_ordenado = np.sort(int_array)

    # 2. Array semi-ordenado (90% ordenado, 10% desordenado)
    array_semi_ordenado = np.sort(int_array)
    num_invertidos = int(tamanho * 0.1)  # Inverter 10% dos elementos
    indices = np.random.choice(tamanho, num_invertidos, replace=False)
    array_semi_ordenado[indices] = np.random.randint(0, max_valor, num_invertidos)  # Substitui por números aleatórios

    # 3. Array desordenado (aleatório)
    array_desordenado = np.copy(int_array)  # O próprio array aleatório já é desordenado

    # 4. Array totalmente desordenado (embaralhado)
    array_totalmente_desordenado = np.copy(array_ordenado)
    np.random.shuffle(array_totalmente_desordenado)  # Embaralha o array ordenado

    return array_ordenado, array_semi_ordenado, array_desordenado, array_totalmente_desordenado

#Copia arrays
def copiar_arrays(array_ordenado, array_semi_ordenado, array_desordenado, array_totalmente_desordenado):
    array_ordenado_copia = array_ordenado.copy()
    array_semi_ordenado_copia = array_semi_ordenado.copy()
    array_desordenado_copia = array_desordenado.copy()
    array_totalmente_desordenado_copia = array_totalmente_desordenado.copy()
    
    return array_ordenado_copia, array_semi_ordenado_copia, array_desordenado_copia, array_totalmente_desordenado_copia 

def pedir_numero_int(mensagem):
    while True:
        try:
            x = int(input(mensagem))
            return x
        except ValueError:
            print("Entrada invalida, tente novamente!")

def tempo(algoritmo,array):
    inicio = time.time()
    if algoritmo == "mergesort":
        merge.sort(array, 0, array.size - 1)
    elif algoritmo == "quicksort":
        quick.sort(array, 0, array.size - 1)
    elif algoritmo == "insertionsort":
        insertion.sort(array)
    else:
        print("Algoritmo não encontrado!")
        return -1
    fim = time.time()
    return fim - inicio

def exibir_tempo_execucao(nome, resultados):
    print(f"Tempos de execução da ordenação - {nome}:")
    print(f"Tempo de execução - Array ordenado: {resultados[0]}")
    print(f"Tempo de execução - Array semi-ordenado: {resultados[1]}")
    print(f"Tempo de execução - Array desordenado: {resultados[2]}")
    print(f"Tempo de execução - Array totalmente desordenado: {resultados[3]}\n")


tam_array = pedir_numero_int("Digite o tamanho do array:")

#Array exatamente iguais para verificar a velocidade da ordenação dos dados para os mesmos elementos
array_ordenado1, array_semi_ordenado1, array_desordenado1, array_totalmente_desordenado1 = gerar_arrays(tam_array)
array_ordenado2, array_semi_ordenado2, array_desordenado2, array_totalmente_desordenado2 = copiar_arrays(
    array_ordenado1, array_semi_ordenado1, array_desordenado1, array_totalmente_desordenado1
)
array_ordenado3, array_semi_ordenado3, array_desordenado3, array_totalmente_desordenado3 = copiar_arrays(
    array_ordenado1, array_semi_ordenado1, array_desordenado1, array_totalmente_desordenado1
)

print("Arrays gerados e copiados com sucesso!")

#Os tempos de execução para cada algoritmo
resultados_mergesort = [
    tempo("mergesort", array_ordenado1),
    tempo("mergesort", array_semi_ordenado1),
    tempo("mergesort", array_desordenado1),
    tempo("mergesort", array_totalmente_desordenado1)
]

resultados_quicksort = [
    tempo("quicksort", array_ordenado2),
    tempo("quicksort", array_semi_ordenado2),
    tempo("quicksort", array_desordenado2),
    tempo("quicksort", array_totalmente_desordenado2)
]

resultados_insertionsort = [
    tempo("insertionsort", array_ordenado3),
    tempo("insertionsort", array_semi_ordenado3),
    tempo("insertionsort", array_desordenado3),
    tempo("insertionsort", array_totalmente_desordenado3)
]


# Exibir os tempos de execução
print(f"Quantidade de valores no array - {tam_array}")
exibir_tempo_execucao("Merge Sort", resultados_mergesort)
exibir_tempo_execucao("Quick Sort", resultados_quicksort)
exibir_tempo_execucao("Insertion Sort", resultados_insertionsort)

