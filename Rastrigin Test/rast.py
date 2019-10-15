import math
import numpy
from datetime import datetime, timedelta
import time
import random

def rast(arg_list):
    sum = 0
    l = len(arg_list)
    for x in arg_list:
        sum = sum + (x**2 - 10 * math.cos(2*math.pi*x))
    return 10 * l + sum


minimum = {
    2 : rast([random.uniform(-5.12, 5.12) for i in range(2)]),
    5 : rast([random.uniform(-5.12, 5.12) for i in range(5)]),
    20 : rast([random.uniform(-5.12, 5.12) for i in range(20)])
}

output = {
    2 : open("rastrigin2.txt", "a+"),
    5 : open("rastrigin5.txt", "a+"),
    20 : open("rastrigin20.txt", "a+")
}

for i in range(1, 31):
    minimum[2] = rast([random.uniform(-5.12, 5.12) for i in range(2)])
    minimum[5] = rast([random.uniform(-5.12, 5.12) for i in range(5)])
    minimum[20] = rast([random.uniform(-5.12, 5.12) for i in range(20)])

    for params_number in [2, 5, 20]:
        it = 0
        end_time = datetime.now() + timedelta(minutes=3)
        while datetime.now() < end_time:
            args = [random.uniform(-5.12, 5.12) for i in range(params_number)]
            result = rast(args)
            if result < minimum[params_number]:
                minimum[params_number] = result
            it = it + 1
        output[params_number].write("%d %f\n" % (it, minimum[params_number]))
        print("N-am crapat %d %d" % (i, params_number))
