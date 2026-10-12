"""
finding pi
by noah lovett
started 10/07/26
"""
import numpy as np
import scipy
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


bf_line = scipy.stats.linregress(np.log10(steps), np.log10(errors))

def extrapolate_error(limit):
    return (limit - bf_line.intercept) / bf_line.slope

print(str(Acircle))
for i in range (1, 11):
    print("Steps needed to get error of 10e-" + str(i) +": 10e" + str(extrapolate_error(-1*i)))

fig, ax = plt.subplots()
ax.plot(steps, areas)
ax.set_xlabel('Step #')
ax.set_ylabel('Pi Approximation')

fig, ax2 = plt.subplots()
ax2.plot(np.log10(steps), errors, color='red', label='Monte Carlo Results')
ax2.set_xlabel('Step # (log base 10)')
ax2.set_ylabel('Error')

fig, ax3 = plt.subplots()
ax3.plot(np.log10(steps), np.log10(errors), color='red', label='Monte Carlo Results')
ax3.plot(np.log10(steps), bf_line.slope * np.log10(steps) + bf_line.intercept, color='blue', label='Best Fit Line')
ax3.set_xlabel('Step # (log base 10)')
ax3.set_ylabel('Error (log base 10)')
plt.show()