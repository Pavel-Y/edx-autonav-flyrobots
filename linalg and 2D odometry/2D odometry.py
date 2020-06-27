import numpy as np
from math import sin, cos
from plot import plot_trajectory

class UserCode:
    def __init__(self):
        self.position = np.array([[0], [0]])
        
    def measurement_callback(self, t, dt, navdata):
        '''
        :param t: time since simulation start
        :param dt: time since last call to measurement_callback
        :param navdata: measurements of the quadrotor
        '''
        
        #self.position[0] += cos(navdata.rotZ) * navdata.vx * dt - sin(navdata.rotZ) * navdata.vy * dt
        #self.position[1] += sin(navdata.rotZ) * navdata.vx * dt + cos(navdata.rotZ) * navdata.vy * dt
        
        cs = cos(navdata.rotZ)
        sn = sin(navdata.rotZ)
        R = np.array([[cs, -sn], [sn, cs]])
        v = np.array([[navdata.vx, navdata.vy]]).transpose()
        move = np.dot(R, v) * dt
        self.position += move
        
        # TODO: update self.position by integrating measurements contained in navdata
        plot_trajectory("odometry", self.position)

#Navdata
#The navdata contains the following values:
#
#rotX - roll angle in radians (rotation around x axis)
#rotY - pitch angle in radians (rotation around y axis)
#rotZ - yaw angle in radians (rotation around z axis)
#vx - velocity along the x axis (local)
#vy - velocity along the y axis (local)