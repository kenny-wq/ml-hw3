import math
import numpy as np
from random_data_generator import *

def sequential_estimator(mu, var):
    print(f"Data point source function: N({mu}, {var})")

    i = 1
    while True:
        new_data = random_data_generator(mu, math.sqrt(var))

        if i==1:
            pre_sum = new_data
            pre_m2 = 0
            vari = 0
            mean = new_data
        else:
            sum = pre_sum + new_data
            mean = sum/i

            m2 = pre_m2 
            m2 += (new_data-(pre_sum/(i-1)))*(new_data-mean)
            vari = m2/(i-1)

            pre_sum = sum
            pre_m2 = m2


        print(f"Add data point: {new_data}")
        print(f"Mean = {mean} Variance = {vari}")

        if abs(mean-mu) < 0.01 and abs(vari-var) < 0.01:
            break

        i+=1
    
    return i

        
        
       
if __name__=="__main__":
    total_round = sequential_estimator(3,5)

    print(total_round)
