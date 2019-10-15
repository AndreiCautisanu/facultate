import math
import numpy
from datetime import datetime, timedelta
import time
import random


def rosembrock(arg_list):
    sum = 0

    for i in range(0, len(arg_list) - 1):
        sum += 100*(arg_list[i+1] - arg_list[i]**2)**2 + (arg_list[i] - 1)**2

    return sum

minimum = {
    2 : rosembrock([random.uniform(-2.048, 2.048) for i in range(2)]),
    5 : rosembrock([random.uniform(-2.048, 2.048) for i in range(5)]),
    20 : rosembrock([random.uniform(-2.048, 2.048) for i in range(20)])
}

output = {
    2 : open("rosembrock2.txt", "a+"),
    5 : open("rosembrock5.txt", "a+"),
    20 : open("rosembrock20.txt", "a+")
}



for i in range(1, 31):
    minimum[2] = rosembrock([random.uniform(-2.048, 2.048) for i in range(2)])
    minimum[5] = rosembrock([random.uniform(-2.048, 2.048) for i in range(5)])
    minimum[20] = rosembrock([random.uniform(-2.048, 2.048) for i in range(20)])

    for params_number in [2, 5, 20]:
        it = 0
        end_time = datetime.now() + timedelta(minutes=3)
        while datetime.now() < end_time:
            args = [random.uniform(-2.048, 2.048) for i in range(params_number)]
            result = rosembrock(args)
            if result < minimum[params_number]:
                minimum[params_number] = result
            it = it + 1
        output[params_number].write("%d %f\n" % (it, minimum[params_number]))
        print("N-am crapat %d %d" % (i, params_number))
