import matplotlib.pyplot as plt
import numpy as nu
import math

x = nu.linspace(0, 20, 1000, True)

print(x)

plt.plot(x, nu.sin(x))
plt.show()