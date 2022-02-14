# TODO: check collision happen or not
import numpy as np 
def collision(tree, new_point, obs_pos,R):
	r = R + 3
	(N,k) = np.shape(obs_pos)
	flag = 0
	# new point in obstacles or safe area or not
	for i in range(N):
		dis_x = new_point[0] - obs_pos[i][0]
		dis_y = new_point[1] - obs_pos[i][1]
		dis = dis_x**2 + dis_y**2
		if (dis < r**2):
			flag = flag + 1
		else:
			flag = flag
	# moving toward new point
	if (flag == 0):
		for i in range(5):
			dist_x = new_point[0] - tree[0]
			dist_y = new_point[1] - tree[1]
			stepi = np.array([tree[0] + dist_x/5 , tree[1] + dist_y/5])
			for j in range(N):
				dist_obs_x = stepi[0] - obs_pos[j][0]
				dist_obs_y = stepi[1] - obs_pos[j][1]
				dist_obs = dist_obs_x**2 + dist_obs_y**2
				if (dist_obs < r**2):
					flag = flag + 1
				else:
					flag = flag
	return flag