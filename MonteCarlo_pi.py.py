import random
import math
import os

total_point = 0
in_circle = 0
while total_point < 1000000:
    x = int.from_bytes(os.urandom(8), byteorder="big") / ((1 << 64) - 1)
    y = int.from_bytes(os.urandom(8), byteorder="big") / ((1 << 64) - 1)
    total_point = total_point + 1
    if (x**2)+(y**2) <= 1:
        in_circle = in_circle + 1
estimated_pi = ((4*in_circle)/total_point)
print("Estimated pi: ", estimated_pi, "\tTrue pi: ", math.pi)
print("Error: ", (math.pi - estimated_pi))