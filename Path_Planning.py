# TODO: Path planning
import numpy as np 
import matplotlib.pyplot as plt
import Extend_Tree
import MinPath
import Tree_Plot
import Obstacles_Plot

def RRT(start, target, obs_pos, r, env_corner1, env_corner2, R):

	start_node = np.array([[start,0,0,0]],dtype=object)
	target_node = np.array([[target,0,0,0]],dtype=object)

	tree = start_node

	samples = 5000 # sample times

	plot_tree = 0
	for i in range(samples):
		tree = Extend_Tree.extendtree(tree, target_node, obs_pos, r, env_corner1, env_corner2)
		if i == samples*0.1:
			print("10%")
			
		elif i == samples*0.2:
			print("20%")
			if plot_tree == 0:
				tree2 = tree
		elif i == samples*0.3:
			print("30%")

		elif i == samples*0.4:
			print("40%")
			if plot_tree == 0:
				tree4 = tree
		elif i == samples*0.5:
			print("50%")

		elif i == samples*0.6:
			print("60%")
			if plot_tree == 0:
				tree6 = tree
		elif i == samples*0.7:
			print("70%")

		elif i == samples*0.8:
			print("80%")
			if plot_tree == 0:
				tree8 = tree
		elif i == samples*0.9:
			print("90%")

		elif i == samples-1:
			print("DONE!")
			if plot_tree == 0:
				tree10 = tree

	if plot_tree == 0:
		
		Tree_Plot.treeplot(tree2,plot_tree, obs_pos, r, R)
		
		Tree_Plot.treeplot(tree4,plot_tree, obs_pos, r, R)
		
		Tree_Plot.treeplot(tree6,plot_tree, obs_pos, r, R)
		
		Tree_Plot.treeplot(tree8,plot_tree, obs_pos, r, R)
		
		Tree_Plot.treeplot(tree10,plot_tree, obs_pos, r, R)







	(N,k) = np.shape(tree)
	count = 0
	for i in range(N):
		if (tree[i][1]==1):
			count = count+1

	if (count>0): 
		path = MinPath.findpath(tree, target_node)
		return path
	else:
		print("Try again!") # cannot find end node
