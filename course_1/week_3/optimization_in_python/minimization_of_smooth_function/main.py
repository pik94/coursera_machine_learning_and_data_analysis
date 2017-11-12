# coding: utf-8
# Python's version: 3.5
# Задача 1: минимизация гладкой функции

import numpy as np
from math import sin, exp
from scipy.optimize import minimize
from matplotlib import pyplot as plt


def plot(x, y, x_name, y_name):
    """
    Метод строит график данных y=f(x).
    :param x: list, ndarray или другой подобный тип
    :param y: list, ndarray
    :param x_name: string
    :param y_name: string
    :return: None
    """
    plt.plot(x, y)
    plt.xlabel(x_name)
    plt.ylabel(y_name)
    plt.show()
    return


def f(x):
    """
    Вычисляет значение функции f(x) в точке x.
    :param x: array или ndarray type
    :return: значение f(x) в точке x
    """
    return sin(x[0] / 5) * exp(x[0] / 10) + 5 * exp(-x[0] / 2)


if __name__ == "__main__":
    x_0 = int(input("BFGS: Write x_0: "))
    res = minimize(f, np.array([x_0]), method="BFGS")
    x_min = res.x
    y_min = f(x_min)

    print("ndev = {}".format(res.nfev))
    print("nit = {}".format(res.nit))
    print("x_min = {}".format(x_min))
    print("f(x_min) = {}".format(round(y_min, 2)))

    # строить график функции f(x)
    x_array = [x for x in np.arange(1, 30, 0.1)]
    plot(x_array, [f([x]) for x in x_array], "x", "y")

