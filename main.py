import math
from decimal import *


class Function:
    def __init__(self, variable):
        self.variable = variable

    def count(self):
        raise NotImplementedError("Subclass must implement abstract method")


class Sin(Function):

    def count(self):
        gradus = self.variable % (360)
        self.variable = gradus/180*math.pi
        i, lasts, s, fact, num, sign = 1, 0, self.variable, 1, self.variable, 1
        while s != lasts:
            lasts = s
            i += 2
            fact *= i * (i-1)
            num *= self.variable * self.variable
            sign *= -1
            s += num / fact * sign
        return +s


class Cos(Function):
    def count(self):
        gradus = self.variable % (360)
        self.variable = gradus/180*math.pi
        i, lasts, fact, num, sign = 0, 0, 1, self.variable, 1
        s = self.variable**i
        while s != lasts:
            lasts = s
            i += 2
            fact *= i * (i)
            num *= self.variable * self.variable
            sign *= -1
            s += num / fact * sign
        return +s


sinus = Sin(90)
cosinus = Cos(90)
print(sinus.count())
print(cosinus.count())
