import matplotlib.pyplot as plt
from numpy import arange, sin, cos, pi

x = arange(0, 2*pi, 0.1)  # range of x values

sin_x = [sin(x) for x in x]
plt.plot(x, sin_x, label='sin(x)')

cos_x = [cos(x) for x in x]
plt.plot(x, cos_x, label='cos(x)')

plt.axhline(y=0, color='black', linewidth='1')  # axhline: axis horizontal line

plt.fill_between(x, sin_x, 0, alpha=.25)  # alpha: fades the colors
plt.fill_between(x, cos_x, 0, alpha=.25)

plt.xlabel('x values')
plt.ylabel('y values')
plt.title('A Beautiful Graph')
plt.legend()  # legend(): shows labels

plt.grid(alpha=.25)
plt.tight_layout()  # helps to plot in nicer way
plt.savefig('sin-cos')  # saves the graph to the current directory as .png file
plt.show()  # shows graph
