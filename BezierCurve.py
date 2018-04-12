import math
import numpy

def generate_curve(x0, y0, x1, y1, x2, y2, x3, y3, step):
    # step is the number of points on the curve + 1 for t = 0,
    __file_name__ = "test"
    file = open(__file_name__ + ".csv","a")
    file.truncate(0)
    file.write('x0,y0,x1,y1,x2,y2,x3,y3\n')
    file.write(str(x0) + ',' +  str(y0) + ',' + str(x1) + ',' + str(y1) + ',' + str(x2) + ',' + str(y2) + ',' + str(x3) + ',' + str(y3) + '\n')
    file.write('\n')
    file.write('t,x,y,angle\n')
    t = 0
    a = 0
    t_list = []
    x_list = []
    y_list = []
    angle = 0
    angle_list = []
    prev_x = 0
    prev_y = 0
    while t != 1:
        t = a/step
        x = (x0*(1-t)**3) + (3*x1*t*(1-t)**2) + (3*x2*(1-t)*t**2) + (x3*t**3)
        y = (y0*(1-t)**3) + (3*y1*t*(1-t)**2) + (3*y2*(1-t)*t**2) + (y3*t**3)
        delta_x = x-prev_x
        delta_y = y - prev_y
        if delta_x == 0:
            if delta_y > 0:
                angle = 0
            elif delta_y < 0:
                angle = 180
        elif delta_y == 0:
            if delta_x > 0:
                angle = 90
            elif delta_y < 0:
                angle = -90
        else:
            angle = math.atan2(delta_y, delta_x)
            angle = math.degrees(angle)
        if t == 0:
            angle = 0
        else:
            angle = -((angle -270) % 360) + 180
        file.write(str(t) + ',' + str(x) + ',' + str(y) + ',' + str(angle) + '\n')
        t_list.append(t)
        x_list.append(x)
        y_list.append(y)
        angle_list.append(angle)
        file.close
        a += 1
        prev_x = x
        prev_y = y
        print(t)
    print('done')
    print(t_list)
    print(x_list)
    print(y_list)
    print(angle_list)


generate_curve(0, 0, 0, 5, 5, 5, 5, 10, 100)
