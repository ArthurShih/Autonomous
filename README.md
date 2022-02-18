# Autonomous Agent Control
## TODO:
###### Setting a start point and an end point for our agent, and there are several fixed obstacles in the environment. Our agent not only has to pass through those obstacles without collision, it also needs to find the shortest path from start poiunt to end point. 
### Generate environment:
###### The map that our agent need to pass is a 100 by 100 environment. it starts from (5,5) and reaches goal when it arrives (99,99). 14 obstacles are on the map, and I let all obstacles be circular with radius 3 for convenience. All obstacles have 3 additional radius unit safe area, which means our agent not only cannot collide obstacles, but also not allowed to enter safe area.
##### Environment:
![env](https://github.com/ArthurShih/Autonomous_agent_python/blob/main/figure/Environment.png)
###### .
### Path planning
#### Extend tree:
###### First, we find a random point on the map, and then remember the point if our agent moving toward the random point for a step unit as new point (node 1). For this new point, we label it by 1, which means our agent is able to arrive this point(node 1) by moving "1" unit. Notice: new random point is not the new point that we remembered.
###### Next, we find another random point on the map, and then compare our start point with the remembered point (node 1), which one is closer to this new random point. 
###### If the remembered point(node 1) is closer to this new random point, we'll remember anothor new point(node 2) which is the point that if our agent moves from previous remembered point(node 1) toward this new random point for a step unit, and then label this newpoint(node 2) by 2. The label "2" means our agent arrives here by moving 2 unit follows the shortest path. 
###### If start point is closer to this new random point, we'll remember anothor new point(node 1') which is the point that if our agent moves from start point toward this new random point for a step unit, and also label this newpoint(node 1') by 1. The label "1" means our agent arrives here by moving 1 step unit follows the shortest path.
###### As we sampling new random points, a new point generates in each sample. Besides, every new point's label shows how our agent arrives here by minimum cost(shortest path). After thousands of sampling, we can connect every new point by its label, and then generate roughly hundreds of paths that start from our start point. 
###### .
#### Collision detection:
###### Every time we generate a new point, collision detection computes the distance between new point and center of obstacle. If the distance is less than safe area's radius, we drop this new point and generate another random point.
###### By applying Extend tree and Collision detection thousands of times, we have roughly hundreds of paths that start from our start point.
###### .
##### Samples 1000 times
![1000](https://github.com/ArthurShih/Autonomous_agent_python/blob/main/figure/1000.png)
##### Samples 2000 times
![2000](https://github.com/ArthurShih/Autonomous_agent_python/blob/main/figure/2000.png)
##### Samples 3000 times
![3000](https://github.com/ArthurShih/Autonomous_agent_python/blob/main/figure/3000.png)
##### Samples 4000 times
![4000](https://github.com/ArthurShih/Autonomous_agent_python/blob/main/figure/4000.png)
##### Samples 5000 times
![5000](https://github.com/ArthurShih/Autonomous_agent_python/blob/main/figure/5000.png)
###### .
#### Find Minimum path
###### Now, we have tons of paths that starts from start point. To find the minimum cost path that arrives end point, we first find which new point we remembered is less than one step unit from end point. If there are more than one points, we choose the one has minimum cost(shortest path).
###### Last, starts from end point, we connect new points we generated before by their label
##### Minimum Path
![Minpath](https://github.com/ArthurShih/Autonomous_agent_python/blob/main/figure/path.png)
###### .
### PID controller
###### To make our agent follow our desired path, I use PID controller. 
###### First, I cut the desired path into several segements, and each segement has it's own target point. When our agent enter a segement, it follows the path by PID controller until it reaches the target point, and then enter next segement.
###### Our agent is controlled by angle of agent and segement's target point, and Kp = 5, Ki = 0.5, Kd = 0.1.
###### .
###### delta x = V*cos(theta)*dt
###### delta y = V*sin(theta)*dt
###### delta theta = u*dt
###### u = Kp*u + Ki*u_sum + Kd*(du/dt)
###### .
### Result
#### Agent dynamic
![dynamic](https://github.com/ArthurShih/Autonomous_agent_python/blob/main/figure/dynamic.mov)
#### Agent path
![path](https://github.com/ArthurShih/Autonomous_agent_python/blob/main/figure/Figure_6.png)
#### Error
![error](https://github.com/ArthurShih/Autonomous_agent_python/blob/main/figure/error.png)
###### .
### Notice
###### Since every point is generated randomly, simulation may varies. The higher the sample times are, the better the path is. The shorter the step unit is, the smoother the path is.
###### For previous figures, I set sample times = 5000, and step unit = 5
###### If samples 10000 times, and set unit step = 2
##### Agent dynamic
![10000dynamic](https://github.com/ArthurShih/Autonomous_agent_python/blob/main/figure/10000_dynamic.mov)