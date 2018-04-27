import math
import numpy
from BezierCurve import BezierCurve

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

bezier = BezierCurve(0, 0, 0, 5, 5, 5, 5, 10, 100)
bezier_2 = BezierCurve(0, 0, 0, 5, 0, 5, 0, 10, 100)
bezier_3 = BezierCurve(0, 0, 2, 8, 6, 8, 8, 0, 100)
bezier_4 = BezierCurve(0, 0, 10, 10, 0, -15, -5, 5, 100)
# bezier.generate_curve()
# bezier_2.generate_curve()
# bezier_3.generate_curve()
bezier_4.generate_curve()
# bezier.make_csv("test")
# bezier_2.make_csv("line")
bezier_4.make_csv("loopyloop")
