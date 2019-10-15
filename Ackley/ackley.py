import math
import numpy
from datetime import datetime, timedelta
import time
import random

def ackley(arg_list):
    sum1 = 0
    sum2 = 0
    a = 20
    b = 0.2
    c = 2 * math.pi

    for x in arg_list:
        sum1 += x**2
        sum2 += math.cos(c * x)
    
    term1 = -a * math.exp(-b * math.sqrt(sum1/len(arg_list)))
    term2 = -math.exp(sum2/len(arg_list))

    return term1 + term2 + a + math.exp(1)


minimum = {
    2 : ackley([random.uniform(-32.768, 32.768) for i in range(2)]),
    5 : ackley([random.uniform(-32.768, 32.768) for i in range(5)]),
    20 : ackley([random.uniform(-32.768, 32.768) for i in range(20)])
}

output = {
    2 : open("ackley2.txt", "a+"),
    5 : open("ackley5.txt", "a+"),
    20 : open("ackley20.txt", "a+")
}



for i in range(1, 31):
    minimum[2] = ackley([random.uniform(-32.768, 32.768) for i in range(2)])
    minimum[5] = ackley([random.uniform(-32.768, 32.768) for i in range(5)])
    minimum[20] = ackley([random.uniform(-32.768, 32.768) for i in range(20)])

    for params_number in [2, 5, 20]:
        it = 0
        end_time = datetime.now() + timedelta(minutes=3)
        while datetime.now() < end_time:
            args = [random.uniform(-32.768, 32.768) for i in range(params_number)]
            result = ackley(args)
            if result < minimum[params_number]:
                minimum[params_number] = result
            it = it + 1
        output[params_number].write("%d %f\n" % (it, minimum[params_number]))
        print("N-am crapat %d %d" % (i, params_number))
