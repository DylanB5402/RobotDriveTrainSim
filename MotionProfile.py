import math

''' Uses basic kinematics equations (v = d/t, a = v/t, d = vt * 0.5*at^2) to generate a motion profile using a distance, acceleration, and a velocity
The x axis of the motion profile is time, the y-axis is velocity.'''

class MotionProfileTimeBased(object):

    def __init__(self, distance, cruise_vel, max_accel):
        self.distance = distance
        self.cruise_vel = cruise_vel
        self.max_accel = max_accel
        self.max_accel_time = cruise_vel/max_accel
        self.max_accel_dist = 0.5 * max_accel * self.max_accel_time**2




