from random import choice
from math import floor
""" 
    We define all strategies here. To add one, just define a function that 
    receives an array and returns a number and add it to the 'strategies' dictionary with the desired name
"""


def average(array):
    if len(array) == 0:
        return 0
    return sum(array) / len(array)


def choose(array, chosen=0):
    return array[chosen]


def first(array):
    return choose(array, 0)


def middle(array):
    return choose(array, floor((len(array) - 1)/2))


def last(array):
    return choose(array, len(array) - 1)


def random(array):
    return choice(array)


strategies = {
    'average': average,
    'sum': sum,
    'first': first,
    'last': last,
    'random': random,
    'middle': middle,
}
