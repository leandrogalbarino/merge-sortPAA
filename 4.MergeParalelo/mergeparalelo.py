import numpy as np
import concurrent.futures
import threading
import time
import matplotlib.pyplot as plt

# Variáveis globais para armazenar tempos de execução
thread_times = []
thread_id = 0  # Contador para identificar as threads

# Função para mesclar dois subarrays
def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result

# Função para executar o Mergesort de forma paralela
def parallel_mergesort(arr):
    global thread_id  # Usar a variável global para identificação de threads
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    local_thread_id = thread_id  # Captura o ID da thread local
    thread_id += 1  # Incrementa o ID para a próxima thread

    start_time = time.perf_counter()  # Marca o tempo de início

    with concurrent.futures.ThreadPoolExecutor() as executor:
        print(f"Thread {local_thread_id} iniciando a ordenação do array: {arr}")
        
        # Dividir o trabalho em threads
        left_future = executor.submit(parallel_mergesort, arr[:mid])
        right_future = executor.submit(parallel_mergesort, arr[mid:])
        
        left_sorted = left_future.result()
        right_sorted = right_future.result()

    merged = merge(left_sorted, right_sorted)

    end_time = time.perf_counter()  # Marca o tempo de fim
    elapsed_time = end_time - start_time  # Calcula o tempo decorrido
    thread_times.append((local_thread_id, elapsed_time))  # Adiciona o tempo da thread

    print(f"Thread {local_thread_id} finalizou a mesclagem: {merged} em {elapsed_time:.6f} segundos")
    
    return merged


# Solicitar ao usuário o tamanho do array
array_size = int(input("Digite o tamanho do array: "))
arr = np.random.randint(1, 100, size=array_size).tolist()
print(f"Array original: {arr}")

# Ordenar usando Mergesort Paralelo
sorted_arr = parallel_mergesort(arr)
print(f"Array ordenado: {sorted_arr}")

# Visualizar os tempos de execução das threads
# Extraindo IDs das threads e tempos
thread_ids, times = zip(*thread_times)

# Criar o gráfico de barras
plt.bar(list(map(str, thread_ids)), times)  # Convertendo IDs para string e passando como lista
plt.xlabel('IDs das Threads')
plt.ylabel('Tempo de Execução (segundos)')
plt.title('Tempo de Execução das Threads no Mergesort Paralelo')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
