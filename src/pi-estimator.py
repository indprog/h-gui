# Estimates pi by placing random points on a square
# with an area of 1 and counting the number of
# points inside the circle's quarter arc.
import random


# Functions
def point_is_inside_the_circle(x, y):
    return x * x + y * y <= 1


inside_points = 0

total_points = int(input("Enter the number of iterations: "))

for i in range(total_points):
    x = random.random()
    y = random.random()

    if point_is_inside_the_circle(x, y):
        inside_points += 1


pi = 4.0 * inside_points / total_points
print(f"Estimated pi: {pi}")
