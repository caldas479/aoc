import sys
import networkx as nx
from collections import defaultdict
data = open(sys.argv[1]).read().strip().split('\n')
G = nx.Graph()

for l in data:
	node, nbrs = l.split(':')
	for nbr in nbrs.split():
		G.add_edge(node,nbr)
		G.add_edge(nbr,node)

G.remove_edges_from(nx.minimum_edge_cut(G))
p1,p2 = nx.connected_components(G)

print(len(p1)*len(p2))

