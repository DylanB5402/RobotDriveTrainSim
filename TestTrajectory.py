import math
import matplotlib.pyplot as plt
import NerdyMath

'''Testing the algorithm for NerdyTrajectory with a simple drive forward trajectory'''
class TestTrajectory:

    def __init__(self, length, step, cruise_vel, accel):
        self.step = step
        self.length = length
        self.cruise_vel = cruise_vel
        self.accel = accel
        self.generate_path()
        self.graph()


    def generate_path(self):
        a = 1
        x = 0
        y = 0
        x_list = []
        y_list = []
        vel_list = []
        time_list = []
        prev_x = 0
        prev_y = (a/self.step) * self.length
        prev_velocity = 0
        total_time = 0
        total_dist = 0
        while y!= ((self.step+1)/self.step) * self.length:
            x = 0
            y = (a/self.step) * self.length
            a += 1
            x_list.append(x)
            y_list.append(y)
            distance = NerdyMath.distance_formula(prev_x, prev_y, x, y)
            velocity = math.sqrt(prev_velocity**2 + 2 * self.accel * distance)
            time = (-prev_velocity + math.sqrt(prev_velocity**2 - 4 * 0.5 * self.accel * - distance))/self.accel
            total_time += time
            total_dist += distance
            if velocity > self.cruise_vel:
                velocity = self.cruise_vel
            vel_list.append(velocity)
            time_list.append(time)
        # print(x_list)
        # print(y_list)
        self.time_list = time_list
        self.vel_list = vel_list
        print(time_list)
        print(vel_list)
        print(distance)

    def graph(self):
        plt.plot(self.time_list, self.vel_list)
        plt.xlabel('time')
        plt.ylabel('velocity')
        x_scale = self.time_list[self.step - 1] * 1.25
        y_scale = self.vel_list[self.step - 1]
        plt.axis([0, x_scale, 0, y_scale])
        plt.show()
