import math


class Function:
    def __init__(self, variable):
        self.variable = variable

    def count(self):
        raise NotImplementedError("Subclass must implement abstract method")


class Sin(Function):

    def count(self):
        gradus = self.variable % (360)
        self.variable = gradus/180*math.pi
        print(self.variable)
        i, lasts, s, fact, num, sign = 1, 0, self.variable, 1, self.variable, 1
        while s != lasts:
            lasts = s
            i += 2
            fact *= i * (i-1)
            num *= self.variable * self.variable
            sign *= -1
            s += num / fact * sign
            print(s)
        return +s


class Cos(Function):
    pass


sinus = Sin(90)
print(sinus.count())
