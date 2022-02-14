# TODO: Plot obstacles with safe area
import matplotlib.pyplot as plt
import numpy as np

# plotting obstacles
def obstacles(pos,r,i,axes):
	obs_pos = pos[i]
	obs_r = r
	ob = plt.Circle(obs_pos,obs_r)
	return axes.add_patch(ob)

# plotting safe area
def obstacles_safearea(pos, r, R, i, axes):
	obs_pos = pos[i]
	safe_area_r = r + R
	safe_area = plt.Circle(obs_pos, safe_area_r, color="c", fill = False)
	return axes.add_patch(safe_area)