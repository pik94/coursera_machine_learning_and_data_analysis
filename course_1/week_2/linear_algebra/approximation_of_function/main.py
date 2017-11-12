# coding: utf-8
# Python's version: 3.5
# Задача 2: Аппроксимация функций


from math import sin, exp
import numpy as np
from scipy.linalg import solve
from matplotlib import pyplot as plt


def f(x):
    return sin(x / 5) * exp(x / 10) + 5 * exp(-x / 2)


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


def start_linear_approximation(show_plot=False):
    x_array = [1, 15]
    A = [[1, x_array[0]],
         [1, x_array[1]]]
    b = [f(x) for x in x_array]
    b = np.array(b)
    A = np.array(A)
    coefs = solve(A, b)
    if show_plot:
        plot(x_array, [coefs[0] + coefs[1] * x for x in x_array], "x", "y")
    return


def start_quadratic_approximation(show_plot=False):
    x_array = [1, 8, 15]
    A = [[1, x_array[0], x_array[0] * x_array[0]],
         [1, x_array[1], x_array[1] * x_array[1]],
         [1, x_array[2], x_array[2] * x_array[2]]]
    b = [f(x) for x in x_array]
    b = np.array(b)
    A = np.array(A)
    coefs = solve(A, b)
    if show_plot:
        plot(x_array, [coefs[0] + coefs[1] * x + coefs[2] * (x ** 2) for x in x_array], "x", "y")
    return


def start_third_deg_approximation(show_plot=False):
    x_array = [1, 4, 10, 15]
    A = [[1, x_array[0], x_array[0] * x_array[0], x_array[0] * x_array[0] * x_array[0]],
         [1, x_array[1], x_array[1] * x_array[1], x_array[1] * x_array[1] * x_array[1]],
         [1, x_array[2], x_array[2] * x_array[2], x_array[2] * x_array[2] * x_array[2]],
         [1, x_array[3], x_array[3] * x_array[3], x_array[3] * x_array[3] * x_array[3]]]
    b = [f(x) for x in x_array]
    b = np.array(b)
    A = np.array(A)
    coefs = solve(A, b)
    if show_plot:
        plot(x_array, [coefs[0] + coefs[1] * x + coefs[2] * (x ** 2) + coefs[3] * (x ** 3) for x in x_array], "x", "y")
    return coefs


if __name__ == "__main__":
    # start_linear_approximation(True)
    # start_quadratic_approximation(True)
    coefs = start_third_deg_approximation(True)
    print(list(map(lambda x: x.round(2), coefs)))
