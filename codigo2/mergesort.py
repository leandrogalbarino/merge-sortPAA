import numpy as np
import matplotlib.pyplot as plt

# Armazenar a pilha de chamadas da árvore de recursão
call_stack = []

# Função para mesclar os subarrays (mesma implementação)
def merge(array, left, middle, right):
    n1 = middle - left + 1
    n2 = right - middle

    left_array = np.zeros(n1)
    right_array = np.zeros(n2)

    for i in range(n1):
        left_array[i] = array[left + i]
    for j in range(n2):
        right_array[j] = array[middle + 1 + j]

    i = 0
    j = 0
    k = left

    while (i < n1) and (j < n2):
        if left_array[i] <= right_array[j]:
            array[k] = left_array[i]
            i += 1
        else:
            array[k] = right_array[j]
            j += 1
        k += 1

    while i < n1:
        array[k] = left_array[i]
        i += 1
        k += 1

    while j < n2:
        array[k] = right_array[j]
        j += 1
        k += 1

# Função principal do Merge Sort
def sort(array, left, right):
    if left < right:
        middle = left + (right - left) // 2
        
        # Armazena a chamada atual na pilha
        call_stack.append((left, right))  # Left, right
        
        sort(array, left, middle)
        sort(array, middle + 1, right)
        merge(array, left, middle, right)

# Função para plotar a árvore de recursão
def plot_recursion_tree():
    fig, ax = plt.subplots(figsize=(12, 8))
    
    # Calcula a profundidade máxima da árvore
    max_depth = len(call_stack)

    for i, (left, right) in enumerate(call_stack):
        depth = i  # Profundidade correspondente à ordem de chamada
        ax.text(left + (right - left) / 2, -depth, f'[{left}, {right}]', 
                fontsize=10, ha='center', va='center', bbox=dict(facecolor='white', edgecolor='black', boxstyle='round,pad=0.5'))
        if depth > 0:
            # Conecta ao pai
            parent_left, parent_right = call_stack[(depth - 1)]
            ax.plot([left + (right - left) / 2, parent_left + (parent_right - parent_left) / 2], 
                    [-depth, -(depth - 1)], 'k-')

    ax.set_ylim(-max_depth - 0.5, 0.5)
    ax.set_xlim(-1, len(array) + 1)
    ax.set_title('Árvore de Recursão do Merge Sort', fontsize=14)
    ax.set_xlabel('Posição no Array', fontsize=12)
    ax.set_ylabel('Profundidade da Recursão', fontsize=12)
    ax.axhline(0, color='black', lw=1)
    ax.axis('off')  # Remove eixos
    plt.grid(False)
    plt.show()

# Exemplo de uso
array = np.random.randint(1, 100, size=112)  # Exemplo de array
sort(array, 0, len(array) - 1)  # Chama o Merge Sort
plot_recursion_tree()  # Plota a árvore
