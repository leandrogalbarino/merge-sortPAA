import matplotlib.pyplot as plt
import networkx as nx
import random

# Função para gerar a visualização da árvore de recursão
def plot_mergesort_tree(arr, parent=None, G=None):
    if G is None:
        G = nx.DiGraph()
    
    if len(arr) > 1:
        mid = len(arr) // 2
        
        # Divide o vetor em duas partes
        left = arr[:mid]
        right = arr[mid:]
        
        # Nó do vetor completo
        node = tuple(arr)
        G.add_node(node)
        
        if parent:
            G.add_edge(parent, node)

        # Recursão para as duas metades
        plot_mergesort_tree(left, node, G)
        plot_mergesort_tree(right, node, G)

    else:
        # Quando o vetor tem um elemento, é uma folha
        node = tuple(arr)
        G.add_node(node)
        if parent:
            G.add_edge(parent, node)
    
    return G

# Função para mesclar dois arrays e gerar o gráfico de mesclagem
def plot_merge_tree(left, right, parent_node, G):
    merged = sorted(left + right)
    merged_node = tuple(merged)
    
    # Adiciona os nós e as arestas para a mesclagem
    G.add_node(merged_node)
    G.add_edge(parent_node, merged_node)

    return merged_node

# Função para desenhar quadrados representando os vetores
def desenha_arvore(G, title=""):
    plt.figure(figsize=(10, 10))  # Aumenta o tamanho da figura
    plt.title(title)

    try:
        pos = nx.nx_agraph.graphviz_layout(G, prog='dot')
    except ImportError:
        pos = nx.spring_layout(G)
        print("Usando layout de molas, instale o 'pygraphviz' para melhor visualização.")
    
    # Desenha as arestas (conexões entre os nós)
    nx.draw_networkx_edges(G, pos)

    # Desenha os nós manualmente como quadrados
    for node in G.nodes:
        x, y = pos[node]
        plt.text(x, y, str(list(node)), 
                 ha='center', va='center', bbox=dict(facecolor='lightblue', boxstyle='round,pad=0.5'))

    # Ajusta as margens ao redor da figura
    plt.subplots_adjust(left=0.001, right=0.997, top=1.0, bottom=0.001)
    
    plt.show(block=False)  # Permite que a janela permaneça aberta

# Função para gerar um vetor aleatório
def random_array(size, lower_bound=1, upper_bound=100):
    return [random.randint(lower_bound, upper_bound) for _ in range(size)]

# Solicitar ao usuário o tamanho da lista, limitado a 20 para uma visualização boa
array_size = int(input("Digite o tamanho da lista (máx 20): "))
array_size = min(array_size, 20)
arr = random_array(array_size)

# Exibir a lista gerada
print(f"Array gerado: {arr}")

# Gerar a árvore de recursão
G = plot_mergesort_tree(arr)

# Visualizar a árvore com quadrados (divisão)
desenha_arvore(G, title="Árvore de Divisão do Merge Sort")

# Função de Merge Sort com visualização
def mergesort_with_plot(arr, parent_node, G):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = mergesort_with_plot(arr[:mid], tuple(arr), G)
    right = mergesort_with_plot(arr[mid:], tuple(arr), G)
    
    # Plotar a mesclagem
    plot_merge_tree(left, right, tuple(arr), G)
    
    return sorted(left + right)

# Mesclar e gerar a árvore de mesclagem
G_merge = nx.DiGraph()  # Novo gráfico para mesclagem
mergesort_with_plot(arr, None, G_merge)

# Visualizar a árvore de mesclagem
desenha_arvore(G_merge, title="Árvore de Mesclagem do Merge Sort")

# Para garantir que todas as janelas sejam exibidas
plt.show()
