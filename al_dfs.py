G = {
    '5': ['3', '7'],
    '3': ['2', '4'],
    '7': ['8'],
    '2': [],
    '4': ['8'],
    '8': []
}

vertex = set()
used = {}
N = 0


def dfs(vertex, G, node):
    if node not in vertex:
        print(node)
        vertex.add(node)
        for neighbour in G[node]:
            dfs(vertex, G, neighbour)

dfs(vertex, G, '2')


