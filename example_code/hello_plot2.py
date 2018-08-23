"""
Hello World example

Author: Alexander Hentschel, alex.hentschel@axiomzen.co
"""

import numpy as np

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #
# Change matplotlib backend from "MacOSX" (default) to "TKAgg"
# This should fix a variety of issues under MacOS.
# IMPORTANT: execute in a newly opend Python Console.
# ............................................................................ #
import matplotlib as mpl
mpl.use("TKAgg", warn=False, force=True)

# For making this change permanent, modify your `~/.matplotlib/matplotlibrc`
# as described in the 01_setup_python.md.
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #

import matplotlib.pyplot as plt

def sample_sin(start=0, stop=10, points=10000):
    x = np.linspace(start, stop, num=points)
    y = np.sin(x)
    return x,y

x, y =  sample_sin()

fig = plt.figure()
plt.plot(x,y)
plt.draw()
