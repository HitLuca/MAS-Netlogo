import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import math

names = ['Amstel', 'Amstelveenseweg', 'Buikslotermeer', 'Centraal', 'Dam', 'Evertsenstraat', 'Floradorp', 'Haarlemmermeerstation', 'Hasseltweg', 'Hendrikkade', 'Leidseplein', 'Lelylaan', 'Muiderpoort', 'Museumplein', 'RAI', 'SciencePark', 'Sloterdijk', 'Surinameplein', 'UvA', 'VU', 'Waterlooplein', 'Weesperplein', 'Wibautstraat', 'Zuid']
xs = [27, 11, 31, 22, 21, 11, 25, 11, 26, 25, 17, 4, 31, 17, 19, 35, 6, 10, 38, 14, 23, 24, 25, 15]
ys = [7, 4, 30, 21, 18, 18, 30, 9, 24, 18, 14, 12, 13, 11, 3, 10, 26, 13, 11, 1, 16, 13, 11, 4]
conn = [[22, 15, 14], [11, 19, 23, 7], [8], [16, 4, 20, 9], [3, 5, 10], [4, 16, 10, 17], [8], [1, 17, 13], [2, 6, 9], [3, 8, 20], [4, 5, 17, 13, 21], [1, 16, 17], [20, 15, 22], [7, 10, 22, 23], [0, 23], [0, 12, 18], [3, 5, 11], [5, 7, 10, 11], [15], [1, 23], [3, 9, 12, 21], [10, 20, 22], [0, 12, 13, 21], [1, 13, 14, 19]]

def dist(a, b):
    return math.sqrt((xs[a] - xs[b])**2 + (ys[a] - ys[b])**2) if b in conn[a] or a in conn[b] else math.inf


def prob_matrix(filename):
    with open(filename) as f:
        lines = [l[:-1] for l in f][2:]

    counts = {k: np.zeros(len(names)) for k in names}

    for l in lines:
        l = l.split(';')
        counts[l[1]] += np.array(l[2:], dtype=np.int32)

    res = np.vstack((v for k, v in sorted(counts.items())))
    return res / res.sum()

G = nx.Graph()
G.add_nodes_from(names)
pos = {k: (xs[i], ys[i]) for i, k in enumerate(names)}

for e in names:
    for d in conn[names.index(e)]:
        G.add_edge(e, names[d], weight=dist(names.index(e), d))

distances = np.zeros((len(names), len(names)))

for origin in names:
    result = nx.dijkstra_predecessor_and_distance(G, origin)[1]
    for destination in result:
        distances[names.index(origin)][names.index(destination)] = result[destination]

with open('distances.txt', 'w') as f:
    print(distances, file=f)
