# TODO: Main Function
import numpy as np 
import matplotlib.pyplot as plt
import Obstacles_Plot
import Path_Planning
import PIDTracking

# Environment
env_corner1 = [0,0]
env_corner2 = [100,100]

# Obstacles
Z = [[0,0]]
pos1 = np.array(Z*5,dtype=object)
pos2 = np.array(Z*4,dtype=object)
pos3 = np.array(Z*5,dtype=object)
pos_x = np.linspace(0,100,6)
pos_y = np.linspace(0,100,6)
for i in range(5):
	pos1[i] = [pos_x[i],pos_y[i+1]]
	pos3[i] = [pos_x[i+1],pos_y[i]]
	if i<4:
		pos2[i] = [pos_x[i+1],pos_y[i+1]]
obs_pos = np.concatenate((pos1,pos2,pos3))
(N,k) = np.shape(obs_pos) # N = number of obstacles
r = 3 # radius of obstacles
R = 3 # safe area of obstacles

# Path starting and ending points
start = np.array([5,5])
target = np.array([99,99])

# Path planning
path = Path_Planning.RRT(start, target, obs_pos, r, env_corner1,env_corner2,R)

# Plotting obstacles with safe area
figure, axes = plt.subplots()
for i in range(N):
	Obstacles_Plot.obstacles_safearea(obs_pos, r, R, i, axes)
	Obstacles_Plot.obstacles(obs_pos,r,i,axes)

# Plotting path
(N,k) = np.shape(path)
xdata = np.zeros(N)
ydata = np.zeros(N)
for i in range(N):
	xdata[i] = path[i][0][0]
	ydata[i] = path[i][0][1]
plt.plot(xdata,ydata,'r-')
plt.xlim([0,100])
plt.ylim([0,100])

# PID controller
data = PIDTracking.trackcontroller(xdata,ydata,start,target)
plt.show()

(k,N) = np.shape(data)
t_start = 0
t_end = N
t = np.arange(t_start, t_end, 1)
plt.figure()
plt.subplot(211)
plt.title("error")
plt.plot(t,data[0],"g-")
plt.grid()
plt.subplot(212)
plt.title("u")
plt.plot(t,data[1],"r-")
plt.grid()
plt.show()
