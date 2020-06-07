class Function:
    def __init__(self, variable):
        self.variable = variable

    def count(self, variable):
        raise NotImplementedError("Subclass must implement abstract method")


class Sin(Function):
    pass


class Cos(Function):
    pass
