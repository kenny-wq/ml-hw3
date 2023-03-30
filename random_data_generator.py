import numpy as np
import math
import matplotlib.pyplot as plt


def random_data_generator(mu, sigma) -> np.ndarray:  # box muller method
    u = np.random.rand()
    v = np.random.rand()

    x = math.cos(2*math.pi*v)*math.sqrt(-2*math.log(u))
    x = x*sigma+mu

    return x

def linear_model_data_generator(n,a,w, num: int)->np.ndarray: 
    result = np.zeros(num)

    for k in range(num):
        x = np.random.uniform(-1,1)

        fi_x = np.array([x**i for i in range(n)])

        e = random_data_generator(0,math.sqrt(a),1).item()

        y = np.dot(w,fi_x) + e

        result[k] = y
    
    return result

if __name__=="__main__":
    result = np.zeros(100)
    for i in range(100):
        result[i] = random_data_generator(3,math.sqrt(5))
    
    plt.plot(result)
    plt.show()


