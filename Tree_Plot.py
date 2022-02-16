import numpy as np 
import matplotlib.pyplot as plt
import Obstacles_Plot
def treeplot(tree, plot_tree, obs_pos, r, R):
	(N,k) = np.shape(tree)



	if plot_tree == 0:
		(G,k) = np.shape(obs_pos)
		figure, axes = plt.subplots()
		for i in range(G):
			Obstacles_Plot.obstacles_safearea(obs_pos, r, R, i, axes)
			Obstacles_Plot.obstacles(obs_pos,r,i,axes)

	while N > 0:
		node = np.array([tree[N-1][0]],dtype = object)
		parent_node = tree[N-1][3]
		while parent_node > 1:
			current_parent = parent_node
			current_node = np.array([tree[parent_node][0]],dtype=object)
			branch = np.concatenate((current_node,node))
			parent_node = tree[parent_node][3]
			node = branch

		(P,k) = np.shape(branch)
		treex = np.zeros(P)
		treey = np.zeros(P)
		for i in range(P):
			treex[i] = branch[i][0]
			treey[i] = branch[i][1]
		plt.plot(treex,treey,"g-")

		N=N-1
		
