import math
import numpy
from datetime import datetime, timedelta
import time
import random


def dixonprice(arg_list):
    term1 = (arg_list[0] - 1)**2

    sum = 0
    for i in range(1, len(arg_list)):
        sum += (i+1) * (2 * arg_list[i]**2 - arg_list[i-1])**2

    return term1 + sum


minimum = {
    2 : dixonprice([random.uniform(-32.768, 32.768) for i in range(2)]),
    5 : dixonprice([random.uniform(-32.768, 32.768) for i in range(5)]),
    20 : dixonprice([random.uniform(-32.768, 32.768) for i in range(20)])
}

output = {
    2 : open("dixonprice2.txt", "a+"),
    5 : open("dixonprice5.txt", "a+"),
    20 : open("dixonprice20.txt", "a+")
}



for i in range(1, 31):
    minimum[2] = dixonprice([random.uniform(-32.768, 32.768) for i in range(2)])
    minimum[5] = dixonprice([random.uniform(-32.768, 32.768) for i in range(5)])
    minimum[20] = dixonprice([random.uniform(-32.768, 32.768) for i in range(20)])

    for params_number in [2, 5, 20]:
        it = 0
        end_time = datetime.now() + timedelta(minutes=3)
        while datetime.now() < end_time:
            args = [random.uniform(-32.768, 32.768) for i in range(params_number)]
            result = dixonprice(args)
            if result < minimum[params_number]:
                minimum[params_number] = result
            it = it + 1
        output[params_number].write("%d %f\n" % (it, minimum[params_number]))
        print("N-am crapat %d %d" % (i, params_number))
