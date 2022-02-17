import numpy as np 
import matplotlib.pyplot as plt

def trackcontroller(xdata, ydata, start, target):
	(N,) = np.shape(xdata)
	Kp = 5
	Ki = 0.5
	Kd = 0.1
	V = 1
	dt = 0.1	
	th_d = np.pi/4
	ulim = 1
	start_x = 4
	start_y = 3
	error_data = []
	udata = []
	for i in range(N):
		print(i)
		target_x = xdata[i]
		target_y = ydata[i]
		dist_x = (target_x - start_x)**2
		dist_y = (target_y - start_y)**2
		dist = np.sqrt(dist_x + dist_y)
		error_sum = 0
		th_error_pre = 0
		k = 0
		while (dist > 0.1):
			if (target_x-start_x)<0:
				th_p = np.pi+np.arctan((target_y-start_y)/(target_x-start_x))
			else:
				th_p = np.arctan((target_y-start_y)/(target_x-start_x))

			th_error = th_p - th_d
			error_sum = error_sum + th_error

			u = Kp*th_error + Ki*error_sum + Kd*(th_error-th_error_pre)
			th_error_pre = th_error 

			if np.abs(u*dt > ulim):
				ut = ulim
			else:
				ut = u*dt

			udata.append(ut)

			angle = ut + th_d

			start_x = start_x + V*np.cos(angle)*dt
			start_y = start_y + V*np.sin(angle)*dt 

			th_d = angle
			dist_x = (target_x - start_x)**2
			dist_y = (target_y - start_y)**2
			dist = np.sqrt(dist_x + dist_y)

			error_data.append(th_error)

			plt.plot(start_x,start_y,"ro")
			plt.show(block=False)
			plt.pause(0.00001)


	return [error_data,udata]




