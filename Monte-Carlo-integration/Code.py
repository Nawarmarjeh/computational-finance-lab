import numpy as np 

def integration(f, a, b, n):
    x_rand = np.random.uniform(a, b, n)
    values = f(x_rand)
    ewert = np.mean(values)
    integral = ewert * (b-a)
    return integral

f = lambda x: x**2
a, b = -1, 1
n = 10000

x_rand, ewert, integral = integration(f, a, b, n)
