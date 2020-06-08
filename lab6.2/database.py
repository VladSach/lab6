class Catalog:
    def __init__(self):
        self.base = dict()

    def read_base():
        file = open('base.txt')
        f = file.readlines()
        for i in range(len(f)):
            f[i] = f[i][0:-1]
            f[i] = list(map(int, f[i].split()))
            self.base[f[i][0]] = f[i][1::]

    def add(self, data):
        key = 1
        added = False
        while not added:
            if key not in self.base:
                self.base[key] = [data]
                added = True
            else:
                key += 1

    def write_base(base):
        file = open('base.txt', 'w')
        for key in range(len(self.base)):
            if key in self.base:
                file.write(str(key))
                values = self.base[key]
                for i in values:
                    file.write(' ' + str(i))
                file.write('\n')

    def show():
        for i in self.base:
            print(i)

    def sold(key):
        item = self.base[key]
        self.base["SOLD" + str(key)] = item
        del self.base[key]


class CustomerBase:
    def __init__(self):
        self.base = list()

    def read_base():
        file = open('customer_base.txt')
        f = file.readlines()
        for i in range(len(f)):
            self.base.append(i)


class Customer:
    def __init__(self, name, time, description, conditions):
        self.name = name
        self.time = time
        self.description = description
        self.conditions = conditions
