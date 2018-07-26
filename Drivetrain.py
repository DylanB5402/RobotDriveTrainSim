import math
import matplotlib.pyplot as plt
import NerdyMath
import numpy

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
        self.time = 0
        self.linear_vel = 0
        self.angular_vel = 0

    def update(self, left_vel, right_vel):
        self.left_vel = left_vel
        self.right_vel = right_vel
        self.linear_vel = (left_vel + right_vel)/2
        self.angular_vel = (left_vel - right_vel)/self.width
        delta_pos = self.linear_vel * self.dt
        delta_theta = self.angular_vel * self.dt
        self.robot_pos += delta_pos
        self.robot_angle += delta_theta
        self.right_pos += self.right_vel * self.dt
        self.left_pos += self.left_vel * self.dt
        self.robot_x += delta_pos * math.sin(delta_theta + self.robot_angle)
        self.robot_y += delta_pos * math.cos(delta_theta + self.robot_angle)
        self.x_list.append(self.robot_x)
        self.y_list.append(self.robot_y)
        self.robot_angle_deg = math.degrees(self.robot_angle)
        self.time += self.dt


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
        angle = -(360 - self.robot_angle_deg) % 360
        error = target - angle
        if error >= 180:
            error -= 360
        if error <= -180:
            error += 360
        prev_error = error
        while abs(error) > 0.02:
            angle = -(360 - self.robot_angle_deg) % 360
            error = target - angle
            if error >= 180:
                error -= 360
            elif error <= -180:
                error += 360
            velocity = error * kP + ((error - prev_error) / self.dt) * kD
            self.update(velocity, -velocity)
            prev_error = error



    def drive_at_heading(self, target_angle, kP, distance, straight_velocity):
        angle = -(360 - self.robot_angle_deg) % 360
        error = target_angle - angle
        if error >= 180:
            error -= 360
        if error <= -180:
            error += 360
        straight_error = distance - self.robot_pos
        while abs(straight_error) > 0.02:
            straight_error = distance - self.robot_pos
            angle = -(360 - self.robot_angle_deg) % 360
            error = target_angle - angle
            if error >= 180:
                error -= 360
            elif error <= -180:
                error += 360
            rot_velocity = error * kP
            self.update(straight_velocity + rot_velocity, straight_velocity - rot_velocity)

    def arc_turn(self, target, kP, power_right, direction):
        angle = -(360 - self.robot_angle_deg) % 360
        error = target - angle
        if error >= 180:
            error -= 360
        if error <= -180:
            error += 360
        while abs(error) > 0.02:
            angle = -(360 - self.robot_angle_deg) % 360
            error = target - angle
            if error >= 180:
                error -= 360
            elif error <= -180:
                error += 360
            velocity = abs(error * kP) * numpy.sign(direction)
            # velocity = error * kP
            if power_right:
                self.update(0, velocity)
            else:
                self.update(velocity, 0)

    def radius_turn(self, radius, velocity, distance, turn_right):
        error = distance - self.robot_pos
        while abs(error) > 0.02:
            error = distance - self.robot_pos
            inner_vel = velocity * (radius - (self.width/2))/(radius + (self.width/2))
            if turn_right:
                self.update(velocity, inner_vel)
            else:
                self.update(inner_vel, velocity)

    def drive_motion_profile(self, target_distance, cruise_vel, max_accel):
        max_accel_time = cruise_vel / max_accel
        max_accel_dist = 0.5 * max_accel * max_accel_time ** 2
        accel_time = math.sqrt(target_distance / max_accel)
        if target_distance < 2 * max_accel_dist:  # if motion profile is triangular
            is_trapezoidal = False
            accel_time = math.sqrt(target_distance / max_accel)
            cruise_time = 0
        else:  # if motion profile is trapezoidal
            accel_time = math.sqrt((2 * max_accel_dist) / max_accel)
            cruise_distance = target_distance - (2 * max_accel_dist)
            cruise_time = (cruise_distance / cruise_vel) + accel_time
            is_trapezoidal = True
        start_time = self.time
        time = self.time - start_time
        # print('total time', cruise_time + 2 * accel_time)
        while time < cruise_time + 2 * accel_time :
            time = self.time - start_time
            if is_trapezoidal:
                if time <= accel_time:
                    velocity_output = max_accel * time
                elif time > accel_time and time < cruise_time:
                    velocity_output = cruise_vel
                elif time >= cruise_time:
                    velocity_output = -max_accel * (time - accel_time - cruise_time)
                velocity_output
            else:
                if time <= accel_time:
                    velocity_output = max_accel * time
                elif time > accel_time:
                    velocity_output = - max_accel * (time - accel_time) + (max_accel * accel_time)
            self.update(velocity_output, velocity_output)

    def drive_to_xy(self, x, y, straight_velocity, kP):
        start_time = self.time
        while NerdyMath.distance_formula(x, y, self.robot_x, self.robot_y) >= 2 and self.time - start_time < 1000:
            target_angle = math.degrees(math.atan2(x - self.robot_x, y - self.robot_y))
            angle = -(360 - self.robot_angle_deg) % 360
            error = target_angle - angle
            if error >= 180:
                error -= 360
            elif error <= -180:
                error += 360
            rot_velocity = error * kP
            self.update(straight_velocity + rot_velocity, straight_velocity - rot_velocity)





