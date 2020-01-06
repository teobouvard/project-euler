import networkx as nx

pyramid = '''
75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23
'''.split('\n')[1:-1]

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

