# TODO: Path planning
import numpy as np 
import Extend_Tree
import MinPath

def RRT(start, target, obs_pos, r, env_corner1,env_corner2):

	start_node = np.array([[start,0,0,0]],dtype=object)
	target_node = np.array([[target,0,0,0]],dtype=object)

	tree = start_node

	samples = 8000 # sample times

	for i in range(samples):
		print(i) # tracking sample time
		new_tree = Extend_Tree.extendtree(tree, target_node, obs_pos, r, env_corner1, env_corner2)
		tree = new_tree

	(N,k) = np.shape(tree)
	count = 0
	for i in range(N):
		if (tree[i][1]==1):
			count= count+1

	if (count>0): 
		path = MinPath.findpath(tree, target_node)
		return path
	else:
		print("Try again!") # cannot find end node
