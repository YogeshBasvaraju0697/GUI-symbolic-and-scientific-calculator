import scipy as sp

import matplotlib.pyplot as plt
from sympy import *
import numpy as np
from scipy.misc import derivative


# first method



def function(fun):
        list = []
        exp = ""
        # linspace arguments are (start, stop, number_of_step)
        x = np.linspace(-np.pi, np.pi, 200)

        for i in range(len(fun)):
                list.append(fun[i])
        print(list)

        for i in list:
                if i.isalpha() and i != "x":
                        exp += i
        print(exp)

        if exp == "sin":
             y = np.sin(x)
        elif exp == "cos":
            y = np.cos(x)
        elif exp == "tan":
            y = np.tan(x)


        plt.plot(x, y)
        return x, y


#

# 2nd Method
import numpy as np
from numpy import sin, cos, tan, sinh, cosh, exp,e
import matplotlib.pyplot as plt

def solve_function(expr):
    expr=expr.replace("^", "**")
    print('Parsed function is:',expr)
    func_str='''\
def f(x):
    return ({e})
    '''.format(e=expr)
    exec(func_str, globals())
    return f

def plot(inp):
    fx = solve_function(inp)
    x_range = np.arange(-3,3,0.1)
    plt.plot(x_range,fx(x_range))
    plt.grid(True)
    plt.show()

# fx(x_range)




































