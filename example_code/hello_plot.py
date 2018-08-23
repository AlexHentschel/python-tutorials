"""
Hello World example

Author: Alexander Hentschel, alex.hentschel@axiomzen.co
"""

import numpy as np
import matplotlib.pyplot as plt

def sample_sin(start=0, stop=10, points=10000):
    x = np.linspace(start, stop, num=points)
    y = np.sin(x)
    return x,y

x, y =  sample_sin()

fig = plt.figure()
plt.plot(x,y)
plt.draw()

# Now try to edit the code while KEEPING the PLOT OPEN
# ...
# The plot always stays in front. I found this rather irritating.
# If you like to change that behaviour, see `hello_plot2_.py`
