import math
# VERY WORK IN PROGRESS
# Math on desmos graph here
# https://www.desmos.com/calculator/wzxax8oo7z
''' Uses basic kinematics equations (v = d/t, a = v/t, d = vt + 0.5*at^2) to generate a motion profile using a distance, acceleration, and a cruise velocity
The x axis of the motion profile is time, the y-axis is velocity.'''


class MotionProfileTimeBased(object):

    def __init__(self, distance, cruise_vel, max_accel):
        self.target_distance = distance
        self.cruise_vel = cruise_vel
        self.max_accel = max_accel
        self.max_accel_time = cruise_vel/max_accel
        self.max_accel_dist = 0.5 * max_accel * self.max_accel_time**2
        self.is_trapezoidal = False
        self.accel_time = 0

    def generate_motion_profile(self):
        if self.target_distance < 2 * self.max_accel_dist: # if motion profile is triangular
            self.is_trapezoidal = False
            self.accel_time = math.sqrt(self.target_distance/self.max_accel)
        elif self.target_distance > 2 * self.max_accel_dist: # if motion profile is trapezoidal
            self.accel_time = math.sqrt((2 * self.max_accel_dist)/self.max_accel)
            self.cruise_distance = self.target_distance - (2 * self.max_accel_dist)
            self.cruise_time = (self.cruise_distance/self.cruise_vel) + self.accel_time
            self.is_trapezoidal = True



    def get_velocity(self, time):
        if self.is_trapezoidal:
            print(971)
            if time <= self.accel_time:
                velocity_output = self.max_accel * time
            elif time > self.accel_time and time < self.cruise_time:
                velocity_output = self.cruise_vel
            elif time >= self.cruise_time:
                velocity_output = -self.max_accel * (time - self.accel_time - self.cruise_time)
            return  velocity_output
        else:
            print(254)
            if time <= self.accel_time:
                velocity_output = self.max_accel * time
            elif time > self.accel_time:
                velocity_output = - self.max_accel * (time - self.accel_time) + (self.max_accel * self.accel_time)
            return velocity_output






