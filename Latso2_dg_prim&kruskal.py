graph = {
    'Merak': {'Jakarta': 100},
    'Jakarta': {'Merak': 100, 'Bogor': 60, 'Bandung': 155, 'Cirebon': 250},
    'Bogor': {'Jakarta': 60, 'Bandung': 125},
    'Bandung': {'Bogor': 125, 'Jakarta': 155, 'Cirebon': 130, 'Purwokerto': 130, 'Yogyakarta': 430},
    'Cirebon': {'Jakarta': 250, 'Bandung': 130, 'Purwokerto': 170, 'Semarang': 240},
    'Purwokerto': {'Cirebon': 170, 'Bandung': 130, 'Yogyakarta': 150},
    'Yogyakarta': {'Purwokerto': 150, 'Bandung': 430, 'Solo': 70},
    'Semarang': {'Cirebon': 240, 'Surabaya': 320},
    'Solo': {'Yogyakarta': 70, 'Surabaya': 280, 'Malang': 300},
    'Surabaya': {'Semarang': 320, 'Solo': 280, 'Malang': 90},
    'Malang': {'Surabaya': 90, 'Solo': 300}
}

#  Algoritma Prim 
def prim(graph, start):
    visited = set([start])
    edges = []
    mst = []
    total = 0

    for v, w in graph[start].items():
        edges.append((w, start, v))

    while edges:
        edges.sort()
        w, u, v = edges.pop(0)
        if v not in visited:
            visited.add(v)
            mst.append((u, v, w))
            total += w
            for next_v, next_w in graph[v].items():
                if next_v not in visited:
                    edges.append((next_w, v, next_v))

    return mst, total


#  Algoritma Kruskal 
class DisjointSet:
    def __init__(self, nodes):
        self.parent = {n: n for n in nodes}

    def find(self, node):
        if self.parent[node] != node:
            self.parent[node] = self.find(self.parent[node])
        return self.parent[node]

    def union(self, u, v):
        root_u, root_v = self.find(u), self.find(v)
        if root_u != root_v:
            self.parent[root_v] = root_u

def kruskal(graph):
    edges = []
    for u in graph:
        for v, w in graph[u].items():
            if (v, u, w) not in edges:
                edges.append((u, v, w))
    edges.sort(key=lambda x: x[2])

    ds = DisjointSet(graph.keys())
    mst = []
    total = 0

    for u, v, w in edges:
        if ds.find(u) != ds.find(v):
            ds.union(u, v)
            mst.append((u, v, w))
            total += w

    return mst, total


#  Eksekusi 
prim_mst, prim_total = prim(graph, 'Jakarta')
kruskal_mst, kruskal_total = kruskal(graph)

print("=== Prim ===")
for u, v, w in prim_mst:
    print(f"{u} - {v} = {w}")
print("Total jarak:", prim_total)

print("\n=== Kruskal ===")
for u, v, w in kruskal_mst:
    print(f"{u} - {v} = {w}")
print("Total jarak:", kruskal_total)
