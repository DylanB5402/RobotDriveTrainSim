import math
import NerdyMath
from BezierCurve import BezierCurve
from MotionProfile import MotionProfileTimeBased


class BezierCurveTrajectory(BezierCurve):

    def __init__(self, x0, y0, x1, y1, x2, y2, x3, y3, step, cruise_velocity, acceleration):
        super().__init__(x0, y0, x1, y1, x2, y2, x3, y3, step)
        self.cruise_velocity = cruise_velocity
        self.acceleration = acceleration


    def generateMotionProfile(self):
        motion_profile = MotionProfileTimeBased(self.distance, self.cruise_velocity, self.acceleration)

