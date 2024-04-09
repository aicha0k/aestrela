import time 

# Definindo o mapa como um dicionário de nós e suas conexões
map = {
    'A': {'B': 5, 'C': 10},
    'B': {'A': 5, 'D': 7, 'E': 3},
    'C': {'A': 10, 'E': 6, 'F': 8},
    'D': {'B': 7, 'E': 2, 'G': 12},
    'E': {'B': 3, 'C': 6, 'D': 2, 'F': 4, 'G': 9},
    'F': {'C': 8, 'E': 4, 'H': 6},
    'G': {'D': 12, 'E': 9, 'H': 5},
    'H': {'F': 6, 'G': 5}
}

# Definindo o custo heurístico para cada nó
heuristic = {
    'A': 15,
    'B': 10,
    'C': 12,
    'D': 8,
    'E': 6,
    'F': 8,
    'G': 5,
    'H': 0
}

# Criando uma classe Node para representar um nó no algoritmo A*
class Node:
    def __init__(self, parent=None, position=None):
        self.parent = parent
        self.position = position

        self.g = 0
        self.h = 0
        self.f = 0

    def __eq__(self, other):
        return self.position == other.position

    def __lt__(self, other):
        return self.f < other.f

def aStar(map, start, goal):
    # Criando os nós de início e fim
    start_node = Node(None, start)
    goal_node = Node(None, goal)
    open_list = []
    closed_list = []
    # Adicionando o nó de início na open list
    open_list.append(start_node)

    # O algoritmo deve estar nesse loop enquanto a open list não estiver vazia
    while open_list:
        # Usar o nó com o menor custo f da open list
        current_node = min(open_list, key=lambda x: x.f)
        open_list.remove(current_node)  # Removendo o nó atual da open list
        closed_list.append(current_node)    # Adicionando-o na closed list

        # Verificando se o nó atual é o nó de destino
        if current_node.position == goal_node.position:
            # Começando a salvar o caminho do no de inicio ao no de destino
            path = []
            while current_node is not None:
                path.append(current_node.position)
                current_node = current_node.parent
            path.reverse()
            print("I think I found the path.....")
            time.sleep(2)
            print("Path found: ", path)

            return path

        print("Checking node ", current_node.position)
        time.sleep(2)
        # Pegando os vizinhos do nó atual
        neighbors = map[current_node.position]

        # Iterando sobre os nós vizinhos
        for neighbor_position in neighbors:
            # Criando um nó vizinho
            neighbor_node = Node(current_node, neighbor_position)

            # verificando se o vizinho está na closed list
            if any(closed_child.position == neighbor_node.position for closed_child in closed_list):
                continue

            # calculando os valores das funções g, h e f para o nó vizinho
            neighbor_node.g = current_node.g + neighbors[neighbor_position]
            neighbor_node.h = heuristic[neighbor_node.position]
            neighbor_node.f = neighbor_node.g + neighbor_node.h

            # Verificando se o vizinho está na open list
            if any(open_node.position == neighbor_node.position for open_node in open_list):
                # Encontrando o nó existente na open list
                existing_node = next((x for x in open_list if x.position == neighbor_node.position), None)

                # Verificando se o caminho para o vizinho é melhor
                if neighbor_node.g < existing_node.g:
                    # Atualizando o e o path
                    existing_node.g = neighbor_node.g
                    existing_node.parent = neighbor_node.parent
            else:
                # Adicionando o nó vizinho na open list
                open_list.append(neighbor_node)

    # Se a open list estiver vazia e o nó de destino não foi encontrado, então não há caminho
    return None

# Escolhendo o nó A como nó de início e o nó H como nó de destino, para exemplo
start = "A"
goal = "H"
aStar(map, start, goal)