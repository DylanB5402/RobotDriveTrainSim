import math
import matplotlib.pyplot as plt
import NerdyMath
# VERY WORK IN PROGRESS
# Math on desmos graph here
# https://www.desmos.com/calculator/wzxax8oo7z
''' Uses basic kinematics equations (v = d/t, a = v/t, d = vt + 0.5*at^2, etc) to generate a motion profile using a distance, acceleration, and a cruise velocity
The x axis of the motion profile is time, the y-axis is velocity.'''


class MotionProfileTimeBased(object):

    def __init__(self, distance, cruise_vel, max_accel):
        self.target_distance = distance
        self.cruise_vel = cruise_vel
        self.max_accel = max_accel
        self.max_accel_time = cruise_vel/max_accel
        self.max_accel_dist = 0.5 * max_accel * self.max_accel_time**2
        self.is_trapezoidal = False
        self.accel_time = math.sqrt(self.target_distance/self.max_accel)
        self.generate_motion_profile()
        self.generate_arrays(100)


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
            if time <= self.accel_time:
                velocity_output = self.max_accel * time
            elif time > self.accel_time and time < self.cruise_time:
                velocity_output = self.cruise_vel
            elif time >= self.cruise_time:
                velocity_output = -self.max_accel * (time - self.accel_time - self.cruise_time)
            return velocity_output
        else:
            if time <= self.accel_time:
                velocity_output = self.max_accel * time
            elif time > self.accel_time:
                velocity_output = - self.max_accel * (time - self.accel_time) + (self.max_accel * self.accel_time)
            return velocity_output

    def generate_arrays(self, step):
        if self.is_trapezoidal:
            final_time = self.cruise_time + self.accel_time
        else:
            final_time = 2 * self.accel_time
        self.time_list = []
        self.velocity_list = []
        print(final_time)
        t = 0
        while t <= step:
            time = (t/step) * final_time
            velocity = self.get_velocity(time)
            self.time_list.append(time)
            self.velocity_list.append(velocity)
            t += 1

    def graph(self):
        plt.plot(self.time_list, self.velocity_list)
        plt.xlabel('time')
        plt.ylabel('velocity')
        x_scale = self.time_list[len(self.time_list) - 1] * 1.25
        if self.is_trapezoidal:
            y_scale = self.cruise_vel * 1.25
        else:
            y_scale = self.get_velocity(self.accel_time) * 1.25
        plt.axis([0, x_scale, 0, y_scale])
        plt.show()

class MotionProfilePositionBased(object):

    def __init__(self, distance, cruise_vel, max_accel):
        self.target_distance = distance
        self.cruise_vel = cruise_vel
        self.max_accel = max_accel
        self.max_accel_dist = self.target_distance/2
        self.generate_motion_profile()
        self.generate_arrays(100)

    def generate_motion_profile(self):
        self.accel_dist = (self.cruise_vel ** 2)/ (2 * self.max_accel)
        self.cruise_dist = (self.cruise_vel ** 2)/ (2 * -self.max_accel) + 2 * self.max_accel_dist

    def get_velocity(self, position):
        if position <= self.accel_dist:
            velocity_output = math.sqrt(2 * self.max_accel * position)
        elif position >= self.accel_dist and position <= self.cruise_dist:
            velocity_output = self.cruise_vel
        elif position >= self.cruise_dist and position <= self.target_distance:
            velocity_output = math.sqrt(-2 * self.max_accel * (position - 2 * self.max_accel_dist))
        return velocity_output

    def generate_arrays(self, step):
        self.position_list = []
        self.velocity_list = []
        t = 0
        while t <= step:
            position = (t / step) * self.target_distance
            velocity = self.get_velocity(position)
            self.position_list.append(position)
            self.velocity_list.append(velocity)
            t += 1

    def graph(self):
        plt.plot(self.position_list, self.velocity_list)
        plt.xlabel('position')
        plt.ylabel('velocity')
        x_scale = self.target_distance * 1.25
        y_scale = self.get_velocity(self.target_distance/2) * 1.25
        plt.axis([0, x_scale, 0, y_scale])
        plt.show()






