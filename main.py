"""
finding pi
by noah lovett
started 10/07/26
"""
import numpy as np

rng = np.random.default_rng()
import matplotlib.pyplot as plt

step = int(1e7)
M = 0
N = 0
Asquare = 2 * 2

areas = []
steps = []
errors = []
for i in range(step):
    x = 2 * rng.random() - 1
    y = 2 * rng.random() - 1
    N += 1
    if x ** 2 + y ** 2 <= 1:
        M += 1
    Acircle = Asquare * (M / N)
    steps.append(1 + i)
    areas.append(Acircle)
    errors.append(np.absolute((Acircle - np.pi)/np.pi))

fig, ax = plt.subplots()
ax.plot(steps, areas)
ax.set_xlabel('Step #')
ax.set_ylabel('Pi Approximation')

print(str(Acircle))

fig, ax2 = plt.subplots()
ax2.plot(np.log10(steps), errors)
ax2.set_xlabel('Step #')
ax2.set_ylabel('Error')
plt.show()

