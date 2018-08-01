import math
import matplotlib.pyplot as plt
import NerdyMath
import numpy
from BezierCurve import  BezierCurve

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


    def set_position(self, x, y):
        self.robot_x = x
        self.robot_y = y

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
        accel_time = math.sqrt(numpy.abs(target_distance)/ max_accel)
        if target_distance < 2 * max_accel_dist:  # if motion profile is triangular
            is_trapezoidal = False
            accel_time = math.sqrt(numpy.abs(target_distance) / max_accel)
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
            if numpy.sign(target_distance) == -1:
                velocity_output = -velocity_output
            self.update(velocity_output, velocity_output)
            print(velocity_output)

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

    def drive_pure_pursuit(self, path : BezierCurve, cruise_vel, max_accel, max_lookahead, min_lookahead, going_forwards, kP):
        target_distance = path.distance
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
        t = 1
        # while (NerdyMath.distance_formula(self.robot_x, path.get_last_x(), self.robot_y, path.get_last_y()) > 2 and t != (len(path.x_list)))or time < 20:

        while time <6.8:
            print(t)
            time = self.time - start_time
            lookahead = min_lookahead + (self.linear_vel/cruise_vel) * (max_lookahead - min_lookahead)
            x1 = path.x_list[t]
            y1 = path.y_list[t]
            x2 = path.x_list[t+1]
            y2 = path.y_list[t+1]
            distance = path.dist_list[t+1]
            # print(NerdyMath.distance_formula(self.robot_x, x1, self.robot_y, y1))
            slope = (y2 - y1)/(x2 - x1)
            y_int = y2 - slope * x2
            a = (1 + slope**2)
            b = (-2 * self.robot_x) + (2 * slope * (y_int - self.robot_y))
            c = (self.robot_x ** 2) + (y_int - self.robot_y) ** 2 - lookahead ** 2
            # print(slope, y_int)
            # print(a, b, c)
            # print(b**2 - (4 * a * c))
            # print(a,b,c)
            if numpy.sign(b**2 - (4 * a * c)) == -1:
                lookahead = NerdyMath.distance_formula(self.robot_x, x2, self.robot_y, y2)
                c = (self.robot_x ** 2) + (y_int - self.robot_y) ** 2 - lookahead ** 2
                # print(b**2 - (4 * a * c))
            if (numpy.sign(slope) == 1 and going_forwards) or (numpy.sign(slope) == -1 and not going_forwards):
                goal_x = (-b + math.sqrt(b ** 2 - 4 * a * c)) / (2 * a)
            elif (numpy.sign(slope) == -1 and going_forwards) or (numpy.sign(slope) == 1 and not going_forwards):
                goal_x = (-b - math.sqrt(b ** 2 - 4 * a * c)) / (2 * a)
            goal_y = slope * goal_x + y_int
            drive_radius = (lookahead ** 2)/(2 * (goal_x - self.robot_x))
            if is_trapezoidal:
                if time <= accel_time:
                    velocity_output = max_accel * time
                elif time > accel_time and time < cruise_time:
                    velocity_output = cruise_vel
                elif time >= cruise_time:
                    velocity_output = -max_accel * (time - accel_time - cruise_time)
            else:
                if time <= accel_time:
                    velocity_output = max_accel * time
                elif time > accel_time:
                    velocity_output = - max_accel * (time - accel_time) + (max_accel * accel_time)

            velocity_output = cruise_vel
            inner_vel = velocity_output * (drive_radius - (self.width / 2)) / (drive_radius + (self.width / 2))
            # target_angle = math.degrees(math.atan2(goal_x - self.robot_x, goal_y - self.robot_y))
            # angle = -(360 - self.robot_angle_deg) % 360
            # error = target_angle - angle
            # if error >= 180:
            #     error -= 360
            # elif error <= -180:
            #     error += 360
            # rot_velocity = error * kP
            if numpy.sign(drive_radius) == -1:
                self.update(inner_vel, velocity_output)
            else:
                self.update(velocity_output, inner_vel)
            print('time', time)
            # self.update(velocity_output + rot_velocity, velocity_output - rot_velocity)
            # print(NerdyMath.distance_formula(self.robot_x, x2, self.robot_y, y2))
            # print(self.robot_x, self.robot_y)
            # print(x1, y1, x2, y2)
            if NerdyMath.distance_formula(self.robot_x, self.robot_y, x2, y2) < 2:
                print('yessss')
                t = t + 1
        plt.plot(self.x_list, self.y_list)
        plt.plot(path.x_list, path.y_list)
        plt.xlabel('x')
        plt.ylabel('y')
        plt.axis([-100, 100, -100, 100])
        plt.legend(['robot position', 'path'])
        plt.show()

    def follow_path(self, path : BezierCurve, velocity, kP, kD):
        start_time = self.time + 0.00001
        time = self.time - start_time
        t = 1
        last_time = 0
        last_error = 0
        # while self.robot_pos < path.distance:
        # while time < 3000:
        goal_x = path.x_list[1]
        goal_y = path.y_list[1]
        while (NerdyMath.distance_formula(self.robot_x, self.robot_y, path.get_last_x(), path.get_last_y()) > 2) and t != len(path.y_list):
            print(time)
            print(t)
            time = self.time - start_time
            if t >= len(path.x_list):
                t = len(path.x_list) - 1
            goal_x = path.x_list[t]
            goal_y = path.y_list[t]
            distance = path.dist_list[t]
            target_angle = math.degrees(math.atan2(goal_x - self.robot_x, goal_y - self.robot_y))
            angle = -(360 - self.robot_angle_deg) % 360
            error = target_angle - angle
            if error >= 180:
                error -= 360
            elif error <= -180:
                error += 360
            rot_velocity = error * kP + (error - last_error)/(time - last_time) * kD
            self.update(velocity + rot_velocity, velocity - rot_velocity)
            # if self.robot_pos > distance:
            if NerdyMath.distance_formula(self.robot_x, self.robot_y, goal_x, goal_y) < 2:
                t += 1
            last_error = error
            last_time = time
            # print(t, goal_x, goal_y)
            # print(self.robot_x, self.robot_y)
        plt.plot(self.x_list, self.y_list)
        plt.plot(path.x_list, path.y_list)
        plt.xlabel('x')
        plt.ylabel('y')
        plt.axis([-100, 100, -100, 100])
        plt.legend(['robot position', 'path ' + str(kP) + ',' + str(kD)])
        plt.show()