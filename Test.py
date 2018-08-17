import math
import NerdyMath
from BezierCurve import BezierCurve
from MotionProfile import *
from NerdyTrajectory import NerdyTrajectory
from TestTrajectory import TestTrajectory
from Drivetrain import Drivetrain

bezier = BezierCurve(0, 0, 0, 50, 50, 50, 50, 100, 100)
bezier_reverse = BezierCurve(0, 0, 0, 50, -50, 50, -50, 100, 100)
# bezier.graph()
# bezier_2 = BezierCurve(0, 0, 50, 50, 50, 50, 100, 100, 100)
# bezier_3 = BezierCurve(0, 0, 2, 8, 6, 8, 8, 0, 100)
# bezier_4 = BezierCurve(0, 0, 10, 10, 0, -15, -5, 5, 100)
# bezier_5 = BezierCurve(0, 0, 5, 5, 5, 5, 10, 10, 100)
# print(bezier.distance/100)
print(1)
opposite_scale_auto = BezierCurve(100-100, 0, 150-100, 390, -70-100, 135, -85-100, 300, 375)
# print(opposite_scale_auto.distance/375)
# trajectory_1 = NerdyTrajectory(0, 0, 0, 50, 0, 50, 0, 100, 100, 1, 10, 3)

taco = Drivetrain(10, 0.02)
# taco.turn_to_angle_PID(45, 0.1, 0)
# taco.drive_forward_PID(100, 0.1, 0)
# taco.drive_at_heading(90, 0.01, 1000, 2)
# taco.arc_turn(45, 0.1, False, 1)
# taco.radius_turn(20, 1, 126, False)
# taco.drive_motion_profile(-100, 10, 1)
# taco.drive_to_xy(0, -100, 0.5, 0.01)
# taco.drive_pure_pursuit(bezier, 5, 1, 5, 1, True, 1)
# taco.set_position(100, 0)
# taco.follow_path(bezier, 1, 0.01, 0)
# taco.drive_pure_pursuit_2(opposite_scale_auto, 10, 5, 0.1, True)
# taco.drive_forward_PID(100, 0.1, 0)
# print(1)
taco.drive_pure_pursuit_4(opposite_scale_auto, 15, 5, 0, True)
# taco.graph()
# print(1)
# print(bezier_2.get_closest_point(0, 0))