import numpy as np

n = np.random.randint(0,20,15)
print("the origin one is ")
print(n)
n[n >= n.max()] = 100
print("the result is ")
print(n)