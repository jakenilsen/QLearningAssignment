import numpy as np
import matplotlib.pylab as plt
import networkx as nx

# map cell to cell, add circular cell to goal point
points_list = [(3, 2), (2, 1), (1, 0), (3, 4), (4, 5), (5, 6)]

firstState = 0
finalState = 6

G = nx.Graph()
G.add_edges_from(points_list)
pos = nx.spring_layout(G)
nx.draw_networkx_nodes(G, pos)
nx.draw_networkx_edges(G, pos)
nx.draw_networkx_labels(G, pos)
plt.show()

# how many points in graph? x points
MATRIX_SIZE = 7

# create matrix x*y
R = np.array(np.ones(shape=(MATRIX_SIZE, MATRIX_SIZE)))
R *= -1

# assign zeros to paths and 100 to goal-reaching point
for point in points_list:
    if point[1] == finalState:
        R[point] = 4
    if point[1] == firstState:
        R[point] = 1
    if point[1] != firstState | finalState:
        R[point] = 0

    if point[0] == finalState:
        R[point[::-1]] = 4
    if point[0] == firstState:
        R[point[::-1]] = 1
    if point[0] != firstState or finalState:
        R[point[:: -1]] = 0


# add goal point round trip
R[firstState, firstState] = 1
R[finalState, finalState] = 4

print(R)