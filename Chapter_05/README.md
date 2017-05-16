# Weekly Graded Assignment Instructions

Write a function area_of_circle(r) which returns the area of a circle of radius r

As a refresher, the area of any circle is equal to the radius squared, multiplied by pi (where pi is 3.14159....).

Don’t forget to include the math module, where pi is defined.

import math

def area_of_circle(r):
    r = math.pi * r**2
    return r

area_of_circle