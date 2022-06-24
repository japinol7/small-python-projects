"""Module cell."""
__author__ = 'Joan A. Pinol  (japinol)'

from enum import Enum


class Cell(str, Enum):
    START = 'S'
    GOAL = 'G'
    EMPTY = '·'
    PATH = '*'
    WALL = 'W'
