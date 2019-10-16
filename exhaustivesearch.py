from itertools import combinations_with_replacement as cwr
import numpy
import math
import time

def rast(arg_list):
    sum = 0
    l = len(arg_list)
    for x in arg_list:
        sum = sum + (x**2 - 10 * math.cos(2*math.pi*x))
    return 10 * l + sum


domain5 = cwr(numpy.arange(-5.12, 5.12, 0.2), 5)

minimum = rast([-5.12 for i in range(5)])

start_time = time.time()

for args in list(domain5):
    result = rast(args)
    print(args)
    if result < minimum:
        minimum = result
        args_minimum = args

print("Minim: rastrigin({}) = {}".format(list(args_minimum), minimum))
print(time.time() - start_time)
