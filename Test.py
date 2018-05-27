import math
import NerdyMath
from BezierCurve import BezierCurve
from BezierCurveTrajectory import BezierCurveTrajectory
from MotionProfile import MotionProfileTimeBased


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


# bezier = BezierCurve(0, 0, 0, 5, 5, 5, 5, 10, 100)
# bezier_2 = BezierCurve(0, 0, 0, 5, 0, 5, 0, 10, 100)
# bezier_3 = BezierCurve(0, 0, 2, 8, 6, 8, 8, 0, 100)
# bezier_4 = BezierCurve(0, 0, 10, 10, 0, -15, -5, 5, 100)
bezier_5 = BezierCurve(0, 0, 5, 5, 5, 5, 10, 10, 100)
# motion_profile = MotionProfileTimeBased(50, 5, 1)
# motion_profile.generate_motion_profile()
# print(motion_profile.get_velocity(11))

test = BezierCurveTrajectory(0, 0, 5, 5, 5, 5, 10, 10, 100, 10, 1)


