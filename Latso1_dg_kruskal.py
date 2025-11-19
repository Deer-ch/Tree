#  (Latihan Soal 1) 
edges = [
    ('a', 'c', 1),
    ('e', 'f', 1),
    ('a', 'b', 2),
    ('b', 'c', 3),
    ('c', 'd', 3),
    ('d', 'f', 4),
    ('b', 'd', 5),
    ('c', 'e', 6),
    ('d', 'e', 8)
]

nodes = {'a', 'b', 'c', 'd', 'e', 'f'}
class DisjointSet:
    def __init__(self, nodes):
        self.parent = {n: n for n in nodes}

    def find(self, node):
        if self.parent[node] != node:
            self.parent[node] = self.find(self.parent[node])
        return self.parent[node]

    def union(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)
        if root_u != root_v:
            self.parent[root_v] = root_u

def kruskal(nodes, edges):
    edges.sort(key=lambda x: x[2]) 
    ds = DisjointSet(nodes)
    mst = []
    total_weight = 0

    for u, v, w in edges:
        if ds.find(u) != ds.find(v):
            ds.union(u, v)
            mst.append((u, v, w))
            total_weight += w

    return mst, total_weight

mst, total = kruskal(nodes, edges)

print(" Minimum Spanning Tree (Kruskal) ")
for u, v, w in mst:
    print(f"{u} - {v} = {w}")
print("Total bobot minimum:", total)
