import math
import NerdyMath
from BezierCurve import BezierCurve
from MotionProfile import *
from NerdyTrajectory import NerdyTrajectory
from TestTrajectory import TestTrajectory

def yaw(angle):
    return (360 - angle) % 360


def get_error(desired, actual):
    actual = yaw(actual)
    error = -desired - actual
    if error >= 180:
        error = error - 360
        print(1)
    if error <= -180:
        error = error + 360
    return error


def angle_to_ticks(angle):
    drivetrain_width = 25
    # turning_circle = drivetrain_width *  math.pi
    ticks = math.radians(angle) * 0.5 * drivetrain_width
    return (ticks)


def get_encoder_target(desired, actual):
    error = get_error(desired, actual)
    print(error)
    print(angle_to_ticks(error))

def test_yaw():
    x = -180
    while x != 180:
        print(x, yaw(x))
        x += 1


def calc_xy(left_encoder, right_encoder, angle):
    x = 0
    y = 0
    prev_right = 0
    prev_left = 0
    delta_right = right_encoder - prev_right
    delta_left = left_encoder - prev_left
    average_dist = (delta_left + delta_right)/2
    x = x + average_dist * math.sin(math.radians(angle))
    y = y + average_dist * math.cos(math.radians(angle))
    print(x, y)

def joystick_to_angle(x, y):
    return (math.degrees(math.atan2(y, x)) - 90) * -1

def atan2_to_navx(angle):
    return -((angle -270) % 360) + 180

def test_atan2_to_navx():
    x = -180
    while x != 181:
        print(x, atan2_to_navx(x))
        x += 1

def error_test(desired, actual):
    error = desired - actual
    if error < -180:
        error = error + 180
    if error > 180:
        error = error - 180
    print(desired, actual, error)
    print("separator")


def path_follower_test(x1, y1, x2, y2, x3, y3, lookahead):
    deltaX = x2 - x1
    deltaY = y2 - y1
    distance = NerdyMath.distance_formula(x1, y1, x2, y2)
    slope = deltaY/deltaX
    # print(slope)
    y_intercept = y1 - (slope * x1)
    perpendicular_slope = -(slope ** -1)
    # print(perpendicular_slope)
    y_intercept2 = y3 - (perpendicular_slope * x3)
    x_intersect = (y_intercept2 - y_intercept)/(slope - perpendicular_slope)
    y_intersect = (perpendicular_slope * x_intersect) + y_intercept2
    # print(x_intersect, y_intersect)
    delta_x_target = (deltaX/distance) * lookahead
    x_target = x_intersect + delta_x_target
    y_target = (slope*x_target) + y_intercept
    print(x_target, y_target)

'''uses equations from 254, v = (l+r)/2, w = (r-l)/wheekbase width, w is rad/s, v can be any distance/sec'''
def calc_wheel_velocities(v, w):
    w = -w #negate w, the equation assumes positive is ccw, but navx clockwise is cw
    wheelbase = 10
    l = (2*v - wheelbase * w)/2
    r = 2*v - l
    return l, r

def calc_lookahead(velocity, max_velocity, max_lookahead, min_lookahead):
    return min_lookahead + (velocity/max_velocity) * (max_lookahead - min_lookahead)