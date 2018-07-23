import math
import matplotlib.pyplot as plt
import NerdyMath

class Drivetrain():

    def __init__(self, width, dt):
        self.width = width
        self.robot_angle = 0
        self.left_vel = 0
        self.right_vel = 0
        self.left_pos = 0
        self.right_pos = 0
        self.robot_x = 0
        self.robot_y = 0
        self.dt = dt
        self.robot_pos = 0
        self.x_list = []
        self.y_list = []
        self.robot_angle_deg = 0

    def update(self, left_vel, right_vel):
        self.left_vel = left_vel
        self.right_vel = right_vel
        linear_vel = (left_vel + right_vel)/2
        angular_vel = (left_vel - right_vel)/self.width
        delta_pos = linear_vel * self.dt
        delta_theta = angular_vel * self.dt
        self.robot_pos += delta_pos
        self.robot_angle += delta_theta
        self.right_pos += self.right_vel * self.dt
        self.left_pos += self.left_vel * self.dt
        self.robot_x += delta_pos * math.sin(delta_theta + self.robot_angle)
        self.robot_y += delta_pos * math.cos(delta_theta + self.robot_angle)
        self.x_list.append(self.robot_x)
        self.y_list.append(self.robot_y)
        self.robot_angle_deg = math.degrees(self.robot_angle)


    def graph(self):
        plt.plot(self.x_list, self.y_list)
        plt.xlabel('x')
        plt.ylabel('y')
        plt.axis([-100, 100, -100, 100])
        plt.show()

    def drive_forward_PID(self, target, kP, kD):
        error = target - self.robot_pos
        prev_error = error
        while abs(error) > 0.02:
            error = target - self.robot_pos
            velocity = error * kP + ((error - prev_error)/self.dt) * kD
            self.update(velocity, velocity)
            prev_error = error

    def turn_to_angle_PID(self, target, kP, kD):
        angle = (360 - self.robot_angle_deg) % 360
        error = target - angle
        if error >= 180:
            error -= 360
        if error <= -180:
            error += 360
        prev_error = error
        while abs(error) > 0.02:
            angle = (360 - self.robot_angle_deg) % 360
            error = target - self.robot_angle_deg
            if error >= 180:
                error -= 360
            elif error <= -180:
                error += 360
            velocity = error * kP + ((error - prev_error) / self.dt) * kD
            self.update(velocity, -velocity)
            prev_error = error







