class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for _ in range(vertices)] for _ in range(vertices)]

    def min_key(self, key, mst_set):
        min_val = float('inf')
        min_index = None
        for v in range(self.V):
            if key[v] < min_val and not mst_set[v]:
                min_val = key[v]
                min_index = v
        return min_index

    def prim_mst(self):
        parent = [None] * self.V
        key = [float('inf')] * self.V
        key[0] = 0
        mst_set = [False] * self.V

        parent[0] = -1

        for _ in range(self.V):
            u = self.min_key(key, mst_set)
            mst_set[u] = True

            for v in range(self.V):
                if self.graph[u][v] and not mst_set[v] and key[v] > self.graph[u][v]:
                    key[v] = self.graph[u][v]
                    parent[v] = u

        return sum(self.graph[i][parent[i]] for i in range(1, self.V))


g = Graph(5)
g.graph = [
    [0, 2, 0, 6, 0],
    [2, 0, 3, 8, 5],
    [0, 3, 0, 0, 7],
    [6, 8, 0, 0, 9],
    [0, 5, 7, 9, 0]
]

print("Optimal cost using Prim's algorithm:", g.prim_mst())
