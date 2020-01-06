import networkx as nx

with open('data/p067_triangle.txt') as f:
    pyramid = f.read().split('\n')

pyramid = [line.split() for line in pyramid]
height = len(pyramid) - 1
G = nx.DiGraph()

for h in range(height):
    for i in range(len(pyramid[h])):
        top = pyramid[h][i]
        bottom_left = pyramid[h+1][i]
        bottom_right = pyramid[h+1][i+1]
        name_top = f'{h}_{i}'
        name_bottom_left = f'{h+1}_{i}'
        name_bottom_right = f'{h+1}_{i+1}'
        if h == height - 1:
            G.add_edge(name_bottom_left, name_top, weight=int(top) + int(bottom_left))
            G.add_edge(name_bottom_right, name_top, weight=int(top) + int(bottom_right))
        else:
            G.add_edge(name_bottom_left, name_top, weight=int(top))
            G.add_edge(name_bottom_right, name_top, weight=int(top))

        #print(f'{bottom_left}->{top} & {bottom_right}->{top}')

path = nx.algorithms.dag.dag_longest_path(G)
length = nx.algorithms.dag.dag_longest_path_length(G)
print(path)
print(length)

