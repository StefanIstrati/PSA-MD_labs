import random
import math

def random_point():
    point = random.uniform(0, 2 * math.pi)
    x = math.cos(point)
    y = math.sin(point)
    return x, y

def verify_triangle():
    points = []
    for _ in range(3):
        point = random_point()
        points.extend(point)
    a_x, a_y, b_x, b_y, c_x, c_y = points
    a_b = math.sqrt((b_x - a_x) ** 2 + (b_y - a_y) ** 2)
    a_c = math.sqrt((c_x - a_x) ** 2 + (c_y - a_y) ** 2)
    c_b = math.sqrt((b_x - c_x) ** 2 + (b_y - c_y) ** 2)
    angle_a = math.degrees(math.acos((a_c ** 2 + a_b ** 2 - c_b ** 2) / (2 * a_b * a_c)))
    angle_b = math.degrees(math.acos((a_b ** 2 + c_b ** 2 - a_c ** 2) / (2 * a_b * c_b)))
    angle_c = math.degrees(math.acos((c_b ** 2 + a_c ** 2 - a_b ** 2) / (2 * a_c * c_b)))
    if (angle_a < 90) and (angle_b < 90) and (angle_c < 90):
        return 1
    else:
        return 0

def simulate_triangle(nr_sim):
    x = 0
    for _ in range(nr_sim):
        x += verify_triangle()
    return x / nr_sim

nr_simulare = int(input("nr of simulations: "))
probability = simulate_triangle(nr_simulare)
print(f"probability that triangle has three acute angles is: {probability}")
