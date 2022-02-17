# TODO: Wandering around and then find minimum cost path
import numpy as np 
import random 
import Collision

def extendtree(tree, targetnode, obs_pos, r, env_corner1, env_corner2):
	step_length = 5 # distance that the agent can move every simulation
	flag = 0
	dim = 2 # x and y
	while flag == 0:
		# generate a random point in environment
		random_point = np.ones(dim) 
		random_point = np.array([(env_corner2[0]-env_corner1[0]) * random.random(),(env_corner2[1]-env_corner1[1]) * random.random()])

		(N,k) = np.shape(tree)
		d = np.zeros(N)
		
		# distance between current point and random point
		for i in range(N):
			d[i] = (tree[i][0][0]-random_point[0])**2 + (tree[i][0][1]-random_point[1])**2
		min_dist = min(d)
		ind = np.argmin(d)
		diff = random_point - tree[ind][0]

		# generate new point
		new_point = tree[ind][0] + diff*step_length/np.sqrt(min_dist)

		# collision detection
		if (Collision.collision(tree[ind][0], new_point, obs_pos, r)==0):
			min_cost = (new_point[0]-tree[ind][0][0])**2 + (new_point[1]-tree[ind][0][1])**2
			min_ind = ind
			near_ind = []
			# optimizing path
			for i in range(N):
				dist_x = tree[i][0][0] - new_point[0]
				dist_y = tree[i][0][1] - new_point[1]
				dist = dist_x**2 + dist_y**2
				if (dist<r**2):
					near_ind.append(i)
			(N,) = np.shape(near_ind)
			if (N>1):
				for i in range(N):
					ind = near_ind[i]
					if (Collision.collision(tree[ind][0], new_point, obs_pos, r)==0):
						loc_cost = (new_point[0]-tree[ind][0][0])**2 + (new_point[1]-tree[ind][0][1])**2
						pre_cost = tree[ind][2]
						cost = loc_cost + pre_cost
						if (cost < min_cost):
							min_cost = cost 
							min_ind = ind
			# collecting data of new point and it's previous node
			new_node = np.array([[new_point,0,min_cost,min_ind]],dtype = object)
			new_tree = np.concatenate((tree,new_node))
			flag = 1

	# label the end node
	dist_end_x = targetnode[0][0][0] - new_point[0]	
	dist_end_y = targetnode[0][0][1] - new_point[1]
	dist_end = np.sqrt(dist_end_x**2 + dist_end_y**2)
	if  (dist_end < step_length):
		new_tree[-1][1] = 1 

	return new_tree

