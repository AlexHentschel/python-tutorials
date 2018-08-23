"""
Hello World example

Author: Alexander Hentschel, alex.hentschel@axiomzen.co
"""

import sys


def hello_world():
    """
    Prints a greeting in the console and the location of the currently used Python interpreter.
    """
    p = sys.executable # resolves the current path into an absolute path. Result is a string
    print("Hello World, I am running Python from: '%s'" % p)


hello_world()


