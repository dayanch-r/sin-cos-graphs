import matplotlib.pyplot as plt
from numpy import arange, sin, pi

x = arange(0, 2*pi, 0.1)
sin_x = sin(x)

plt.plot(x, sin_x, label='sin(x)')

plt.title('A Beautiful Graph')
plt.xlabel('x values')
plt.ylabel('y values')

plt.legend()
plt.grid(alpha=.25)

plt.show()
