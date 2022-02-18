# TODO: Optimize path and connect them
import numpy as np 

def findpath(tree,endnode):
	(N,k) = np.shape(tree)
	ind = []
	count = 0
	# how many end node in tree
	for i in range(N):
		if (tree[i][1]==1):
			count = count + 1
			ind.append(i)
	# find the end node with minimum cost
	if (count>0):
		costdata = np.zeros(count)
		for i in range(count):
			index = ind[i]
			costdata[i] = tree[index][2]

		tag = np.argmin (costdata)
		index = ind[tag] 
		node = np.array([tree[index]],dtype=object)
		path = np.concatenate((node,endnode))
		parent_ind = tree[index][3]
		while parent_ind>1:
			pre_node = np.array([tree[parent_ind]],dtype=object)
			path = np.concatenate((pre_node,path))
			parent_ind = tree[parent_ind][3]

	return path
