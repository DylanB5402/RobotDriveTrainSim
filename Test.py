import math
import NerdyMath
from BezierCurve import BezierCurve
from MotionProfile import *
from NerdyTrajectory import NerdyTrajectory
from TestTrajectory import TestTrajectory
from Drivetrain import Drivetrain

# bezier = BezierCurve(0, 0, 0, 5, 5, 5, 5, 10, 100)
# bezier_2 = BezierCurve(0, 0, 0, 5, 0, 5, 0, 10, 100)
# bezier_3 = BezierCurve(0, 0, 2, 8, 6, 8, 8, 0, 100)
# bezier_4 = BezierCurve(0, 0, 10, 10, 0, -15, -5, 5, 100)
# bezier_5 = BezierCurve(0, 0, 5, 5, 5, 5, 10, 10, 100)
# opposite_scale_auto = BezierCurve(100, 0, 160, 390, -70, 135, -85, 290, 30)
# trajectory_1 = NerdyTrajectory(0, 0, 0, 50, 0, 50, 0, 100, 100, 1, 10, 3)

taco = Drivetrain(20, 0.02)
taco.turn_to_angle_PID(-180, 1, 0)
taco.drive_forward_PID(50, 1, 0)
taco.turn_to_angle_PID(90, 1, 0)
taco.drive_forward_PID(100, 1, 0)
taco.graph()

# print(1)